from django.shortcuts import render, redirect,get_object_or_404
from .models import Recipe
from .forms import RecommendationForm
from .recommendation_logic import recommend_recipes
import pandas as pd

def dashboard(request):
    return render(request, 'dashboard.html')

def recommendations(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            # Process the form data and perform recommendation logic
            user_cuisine = form.cleaned_data['cuisine']
            user_diet = form.cleaned_data['diet']
            user_ingredients = form.cleaned_data['ingredients'].split(',')
            user_course = form.cleaned_data['course']

            # Perform recommendation using recommendation_logic.py
            recommended_dishes = recommend_recipes(user_cuisine, user_diet, user_ingredients, user_course)
            
            if recommended_dishes is None:
                # No matching recipes found, handle accordingly
                return render(request, 'no_recipes_found.html')
            else:
                # Convert DataFrame to list of dictionaries
                recommended_dishes = recommended_dishes.to_dict('records')
                
                # Redirect to the recommendations page with recommended dishes
                return render(request, 'recommendations.html', {'recommended_dishes': recommended_dishes})
    else:
        form = RecommendationForm()
    
    return render(request, 'recommendations.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Recipe

# def recipe_details(request, ID):
#     recipe = get_object_or_404(Recipe, ID=ID)
#     return render(request, 'recipe_details.html', {'recipe': recipe})
# def recipe_details(request, ID):
#     recipes = Recipe.objects.filter(ID=ID)
#     if recipes.exists():
#         recipe = recipes.first()
#         return render(request, 'recipe_details.html', {'recipe': recipe})
#     else:
#         # Handle the case where the recipe with the given ID does not exist
#         return render(request, 'recipe_not_found.html')

import pandas as pd
from django.shortcuts import render, get_object_or_404

def recipe_details(request, ID):
    # Read data from CSV file
    data_file = 'final_dataset.csv'
    df = pd.read_csv(data_file)

    # Filter recipe with the specified ID
    recipe_data = df[df['ID'] == ID]

    if not recipe_data.empty:
        # Extract individual recipe details
        cuisine = recipe_data['cuisine'].iloc[0]
        course = recipe_data['course'].iloc[0]
        diet = recipe_data['diet'].iloc[0]
        name = recipe_data['name'].iloc[0]
        description = recipe_data['description'].iloc[0]
        ingredients = recipe_data['ingredients'].iloc[0]
        instructions = recipe_data['instructions'].iloc[0]
        
        # Pass individual recipe details as context
        context = {
            'cuisine': cuisine,
            'course': course,
            'diet': diet,
            'name': name,
            'description': description,
            'ingredients': ingredients,
            'instructions': instructions
        }
        return render(request, 'recipe_details.html', context)
    else:
        # Handle case where recipe with the specified ID is not found
        return render(request, 'recipe_not_found.html')




