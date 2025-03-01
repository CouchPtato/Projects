async function getRecipeDetails() 
{
    const urlParams = new URLSearchParams(window.location.search);
    const mealId = urlParams.get('id');
    const response = await fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${mealId}`);
    const data = await response.json();
    const meal = data.meals[0];

    const instructionsList = meal.strInstructions.split(/\r\n|\n/).filter(line => line.trim() !== "");
    const formattedInstructions = instructionsList.map(step => `<li>${step}</li>`).join('');

    let ingredientsList = '';
    for (let i = 1; i <= 20; i++) 
    {
        const ingredient = meal[`strIngredient${i}`];
        const measure = meal[`strMeasure${i}`];
        
        if (ingredient && ingredient.trim() !== "") 
        {
            ingredientsList += `<li>${measure} ${ingredient}</li>`;
        }
    }

    const detailsDiv = document.getElementById('recipe-details');

    detailsDiv.innerHTML = 
    `
        <h1>${meal.strMeal}</h1>
        <img src="${meal.strMealThumb}" alt="${meal.strMeal}">

        <p> <strong>Category:</strong> ${meal.strCategory} </p>

        <p> <strong>Ingredients:</strong> </p>
        <ul>${ingredientsList}</ul>

        <p> <strong>Instructions:</strong> </p>
        <ul>${formattedInstructions}</ul>

        <a href="${meal.strYoutube}" target="_blank">Watch Video</a>
        <br><br>
        <a href="index.html">Back to Home</a>
    `;
}

window.onload = getRecipeDetails;