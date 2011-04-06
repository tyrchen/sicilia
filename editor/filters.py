# -*- coding: utf-8 -*-
from editor.models import Country

from django.contrib.admin.filterspecs import FilterSpec, ChoicesFilterSpec
from django.utils.translation import ugettext_lazy as _

class CountryFilterSpec(ChoicesFilterSpec):
    def __init__(self, f, request, params, model, model_admin):
        ChoicesFilterSpec.__init__(self, f, request, params, model, model_admin)

        # The lookup string that will be added to the queryset
        # by this filter
        self.lookup_kwarg = 'country__name_en'
        # get the current filter value from GET (we will use it to know
        # which filter item is selected)
        self.lookup_val = request.GET.get(self.lookup_kwarg)

        # Prepare the list of unique, country name, ordered alphabetically
        country_qs = Country.objects.filter(added_by = request.user)
        self.lookup_choices = country_qs.values_list('name_en', flat = True)

    def choices(self, cl):
        # Generator that returns all the possible item in the filter
        # including an 'All' item.
        yield { 'selected': self.lookup_val is None,
                'query_string': cl.get_query_string({}, [self.lookup_kwarg]),
                'display': _('All') }
        for val in self.lookup_choices:
            yield { 'selected' : smart_unicode(val) == self.lookup_val,
                    'query_string': cl.get_query_string({self.lookup_kwarg: val}),
                    'display': val }

    def title(self):
        # return the title displayed above your filter
        return _(u'国家列表')

# Here, we insert the new FilterSpec at the first position, to be sure
# it gets picked up before any other
FilterSpec.filter_specs.insert(0,
  # If the field has a `profilecountry_filter` attribute set to True
  # the this FilterSpec will be used
  (lambda f: getattr(f, 'country_filter', False), CountryFilterSpec)
)
