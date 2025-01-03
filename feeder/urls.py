from django.urls import path
from . import views


urlpatterns = [
    path('contry/', views.ContriesListView.as_view(), name="contry-list"),
    path('contry/create', views.ContryCreateView.as_view(), name="contry-create"),
    path('league/', views.LeaguesListView.as_view(), name="league-list"),
    path('league/contry/<int:pk>', views.LeaguesByContryListView.as_view(), name="league-contry-list"),
    path('league/create', views.LeagueCreateView.as_view(), name="league-create"),
    path('team/league/<int:pk>', views.TeamByLeagueListView.as_view(), name="team-league-list"),
    path('team/create', views.TeamCreateView.as_view(), name="team-create"),
    path('match/team/<int:pk>', views.MatchesByTeamListView.as_view(), name="matches-team-list"),
    path('scraper/update-score', views.scraper_resultados, name="scraper-score"),
    path('scraper/create-league', views.scraper_create_teams, name="scraper-create-league"),
    path('scraper/create-matches', views.scraper_create_matches, name="scraper-create-matches"),
    
]