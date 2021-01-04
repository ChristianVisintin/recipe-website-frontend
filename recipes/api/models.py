# This is free and unencumbered software released into the public domain.
# 
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
# 
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# 
# For more information, please refer to <http://unlicense.org>
#

from django.db import models
from uuid import uuid4

class Tweet(models.Model):
    """
    An imaginary Twitter's tweet entity
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=256)
    nickname = models.CharField(max_length=256)
    date = models.DateTimeField()
    text = models.CharField(max_length=280) # 280 is the maximum tweet length
    url = models.URLField()
    avatar = models.ImageField(upload_to='cache')


class Category(models.Model):
    """
    Category represents a recipe category
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_it = models.CharField(max_length=256)
    name_en = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name_en

class Ingredient(models.Model):
    """
    Ingredient represents an ingredient which can be included in a recipe.
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_it = models.CharField(max_length=256)
    name_en = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name_en

class Recipe(models.Model):
    """
    Recipe represents a recipe, with all its parameters
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title_it = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256)
    date = models.DateTimeField()
    body = models.TextField()
    persons = models.PositiveIntegerField()
    likes = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title_en

# Recipe relations

class RecipeCategory(models.Model):
    """
    RecipeCategory represents a relation between a Category and a Recipe
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class RecipeImage(models.Model):
    """
    RecipeImage represents an image related to a certain recipe
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    file_path = models.ImageField(upload_to='recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.file_path

class RecipeIngredient(models.Model):
    """
    Recipe ingredient is the relation between an Ingredient and a Recipe
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)