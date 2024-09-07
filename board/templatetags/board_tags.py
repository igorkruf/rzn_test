from django import template
from treebeard.forms import movenodeform_factory
# MyNodeForm = movenodeform_factory(Category)


register = template.Library()


@register.simple_tag()
def count_children(node):
    count=node.get_children_count()
    return count

@register.simple_tag()
def get_tree(node):
    list_parents=node.get_tree(node)
    return list_parents


@register.simple_tag()
def get_node_form(node):
    node_form=movenodeform_factory(node)
    return node_form