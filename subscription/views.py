from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import SubscriptionPlan
import json
from django.contrib.auth.decorators import login_required

@login_required
def subscription_plans(request):
    """ Fetch all subscription plans and send them to the frontend """
    plans = SubscriptionPlan.objects.all()
    return render(request, 'subscription/plans.html', {'plans': plans})

def buy_subscription(request, plan_id):
    """ Handle subscription purchase (Placeholder for payment integration) """
    plan = get_object_or_404(SubscriptionPlan, id=plan_id)
    return redirect('/subscription/plans')  # Replace with actual purchase logic

def update_prices(request):
    """ API endpoint to update prices dynamically """
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Load JSON data from request
            country = data.get("country")
            monthly_price = data.get("monthly_price")
            annual_price = data.get("annual_price")
            plan_type = data.get("plan_type")  # Example: 'gold', 'silver', 'bronze'

            if not all([country, monthly_price, annual_price, plan_type]):
                return JsonResponse({"success": False, "message": "Missing required fields"})

            # Fetch the subscription plan
            plan = get_object_or_404(SubscriptionPlan, plan_type=plan_type)

            # Update or add the prices dynamically
            plan.update_prices(country, monthly_price, annual_price)

            return JsonResponse({"success": True, "message": f"Prices updated for {country} in {plan_type} plan"})
        
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON data"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
        
    return JsonResponse({"success": False, "message": "Invalid request method"})
