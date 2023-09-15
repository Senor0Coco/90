"""
como se llama el señor Coco, 
Terminasmos lo basico de esto, varibles es lo que vemos
"""
me_llamo_coco_guardo_esto = "coco"
print (me_llamo_coco_guardo_esto)

me_llamo_coco_guardo_esto = "2+1"
print ("un cambio", me_llamo_coco_guardo_esto)

"""
esto es "input" es pregunta 
"""
me_llamo_coco_guardo_esto = input ("¿como te llamas?")
print ("uso input", me_llamo_coco_guardo_esto)

"""
Tipo de datos
"""
# string es una "me_llamo_coco_guardo_esto"
me_llamo_coco_guardo_esto = "coco"
me_llamo_coco_guardo_esto = 'santiago'
me_llamo_coco_guardo_esto = "21"
print ('me_llamo_coco_guardo_esto =>', me_llamo_coco_guardo_esto)
print (type(me_llamo_coco_guardo_esto))

# int
me_age = 21
print ('my_age =>', me_age)
print(type(me_age))

#booleano
is_single = False
print('is sinble =>', is_single)
print(type(is_single))


# Este es otro tema 
"""
string
"""
name = "moco"
last_name = "molina monroy"
print (name)
print (last_name)


full_name = name + " " + last_name
print(full_name)
quote = "I' m moco"
print(quote)

quote2 = 'She said  Hello" '
print(quote2)

#tipos format o fomas de hacerlo

template = "Hola, mi nombre es" + name + " y mi apellido es" + last_name
print('v1', template)   


template = "Hola, mi nombre es {} y mi apellido es {}". format (name, last_name)
print('v2', template)

template = f" Hola, mi nombre es{name} y me apellido es{last_name}"
print('v3', template)