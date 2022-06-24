from django import templates

regster = template.Library()

@register.filter(name='cut')
def cut(value:arg):
    """
    This cuts all values of "arg " from  the String !
    """
    return value.replace(arg,'')

#register.filter('cut',cut)    
