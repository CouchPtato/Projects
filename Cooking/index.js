async function getCategories() 
{
    const response = await fetch("https://www.themealdb.com/api/json/v1/1/categories.php");
    const data = await response.json();
    const categorySelect = document.getElementById('categories');
    
    data.categories.forEach
    (category => 
        {
            const option = document.createElement('option');

            option.value = category.strCategory;
            option.textContent = category.strCategory;
            categorySelect.appendChild(option);
        }
    );
}

async function getCategoryMeals() 
{
    const category = document.getElementById('categories').value;

    if (!category) 
        return;

    const response = await fetch(`https://www.themealdb.com/api/json/v1/1/filter.php?c=${category}`);

    const data = await response.json();
    displayMeals(data.meals);
}

function displayMeals(meals) 
{
    const recipesDiv = document.getElementById('recipes');
    
    recipesDiv.innerHTML = '';
    
    meals.forEach
    (meal => 
        {
            const recipeDiv = document.createElement('div');

            recipeDiv.classList.add('recipe');
            recipeDiv.innerHTML = 
            `
                <img src="${meal.strMealThumb}" alt="${meal.strMeal}">
                <h3>${meal.strMeal}</h3>
            `;

            recipeDiv.onclick = () => window.location.href = `recipe.html?id=${meal.idMeal}`;
            recipesDiv.appendChild(recipeDiv);
        }
    );
}

window.onload = getCategories;