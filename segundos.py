segundos_str = input('Por favor, entre com o número de segundos que deseja converter: ')
total_segs = int(segundos_str)

segundos_um_dia = 86400
segundos_uma_hora = 3600
segundos_um_minuto = 60

dias = total_segs // segundos_um_dia
segs_restantes = total_segs % segundos_um_dia

horas = segs_restantes // segundos_uma_hora
segs_restantes_minuto = total_segs % segundos_uma_hora

minutos = segs_restantes_minuto // segundos_um_minuto
segs_restantes_final = segs_restantes_minuto % segundos_um_minuto

print(dias, 'dias,', horas,'horas,', minutos, 'minutos e', segs_restantes_final, 'segundos.')