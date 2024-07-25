from django.contrib import admin

from .models import Summoner
# Register your models here.
from .models import CustomUser

admin.site.register(CustomUser)


@admin.register(Summoner)
class SummonerAdmin(admin.ModelAdmin):
    list_display = ('name', 'league_display', 'summoner_level_display')
    search_fields = ('name', 'league__leagueId', 'summoner__puuid')

    # Custom methods to display nested JSON fields in list_display
    def league_display(self, obj):
        return obj.league.get('tier', 'N/A')
    league_display.short_description = 'League Tier'

    def summoner_level_display(self, obj):
        return obj.summoner.get('summonerLevel', 'N/A')
    summoner_level_display.short_description = 'Summoner Level'

    # Show these fields in the admin form
    fields = ('name', 'league', 'summoner', 'mastery', 'matches')
