from django.urls import path
from home import views as home_views
from home import htmx_views

app_name = "home"

urlpatterns = [
    path('', 
        view=home_views.DashboardView.as_view(),
        name="dashboard"
    ),
    path('hide-balance/',
         view=htmx_views.HideBalanceView.as_view(),
         name='hide-balance'
    ),
    path('show-balance/',
         view=htmx_views.ShowBalanceView.as_view(),
         name='show-balance'
    ),
    path('add-money/',
         view=htmx_views.AddMoneyView.as_view(),
         name='add-money'
    ),
    path('wallet/',
        view=htmx_views.WalletView.as_view(),
        name='wallet'
)
]
