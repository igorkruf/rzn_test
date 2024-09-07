from django.db import models
from treebeard.al_tree import AL_Node
from mptt.models import MPTTModel, TreeForeignKey



# Create your models here.

class Cat(MPTTModel):
    ''' Модель категория '''


    name=models.CharField(max_length=250)
    # slug=models.SlugField(blank=True, unique=True, db_index=True)
    parent=TreeForeignKey("self", on_delete=models.CASCADE, related_name="children", blank=True, null=True, db_index=True)
    node_order_by = ['name']


    def __str__(self):
        return self.name
    

    class MPTTMeta:
        order_insertion_by = ['name']


class Genre(MPTTModel):
    '''
    Тестовая модель mptt
    '''
    
    
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
    related_name='children')
    
    
    def __str__(self) -> str:
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
