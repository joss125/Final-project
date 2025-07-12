import discord
import random
from discord.ext import commands

intentions = discord.Intents.default()
intentions.message_content = True

final_bot = commands.Bot(command_prefix="!", intents=intentions)

@final_bot.event
async def on_ready():
    print("Bot en línea")

@final_bot.command()
async def consejo(ctx):
    await ctx.send("¿Deseas ver un consejo sobre como contrarrestar el cambio climático?(si o no)")
    def verificar(m):   #función para asegurarse de que el mensaje sea del mismo autor que ejecutó el comando
        return ctx.author == m.author
    try:
        respuesta_consejo = await final_bot.wait_for('message', check = verificar, timeout = 15) # espera 15 segundos por la respuesta
        dato = respuesta_consejo.content
        dato = dato.lower()
        if dato == "si":
            consejos = ['Usa menos el coche: Camina, usa bicicleta o transporte público para reducir emisiones','Ahorra energía en casa: Apaga luces, usa focos LED y desconecta aparatos que no estés usando','Planta árboles o cuida áreas verdes','Compra productos locales y de temporada: Así se reduce el transporte y la contaminación','Usa botellas, bolsas y recipientes reutilizables','Recicla y separa tu basura','Apoya políticas y proyectos ecológicos']
            random_consejo = random.choice(consejos)
            await ctx.send(f'Podrías: {random_consejo}')
        else:
            await ctx.send("Si deseas un consejo más tarde, avisame.")

    except Exception as e:
        await ctx.send("No recibí una respuesta a tiempo")
        print(f"Error:{e}")

@final_bot.command()
async def dato(ctx):
    await ctx.send("¿Deseas ver un dato curioso sobre el cambio climático?(si o no)")
    def verificar2(m):   #función para asegurarse de que el mensaje sea del mismo autor que ejecutó el comando
        return ctx.author == m.author

    try:
        respuesta_dato = await final_bot.wait_for('message', check = verificar2, timeout = 15) # espera 15 segundos por la respuesta
        dato2 = respuesta_dato.content
        dato2 = dato2.lower()
        if dato2 == "si":
            datos = ['La Tierra está más caliente que nunca en al menos 125,000 años: Estudios paleoclimáticos indican que las temperaturas actuales no tienen precedentes desde la última era interglaciar, hace más de 100 mil años','Los pingüinos emperador podrían desaparecer: Si las emisiones de gases de efecto invernadero continúan al ritmo actual, se estima que el 98% de las colonias de pingüinos emperador podrían desaparecer para el año 2100 debido al derretimiento del hielo antártico','Un solo vuelo de avión puede derretir más de 30 metros cuadrados de hielo ártico: Viajar en avión genera muchas emisiones de CO₂. Por ejemplo, un vuelo redondo entre Nueva York y Londres puede provocar el derretimiento de más de 30 m² de hielo en el Ártico','Las aves están encogiendo: Estudios han demostrado que, debido al aumento de temperaturas, algunas especies de aves han reducido su tamaño corporal, un fenómeno que se considera una adaptación evolutiva al calor','El nivel del mar sube más rápido ahora que en los últimos 3,000 años: El deshielo de glaciares y la expansión térmica del agua hacen que los océanos crezcan a un ritmo alarmante, amenazando a ciudades costeras de todo el mundo','El chocolate, el café y el vino están en peligro: Estos productos dependen de climas específicos. El cambio climático afecta las zonas donde se cultivan, poniendo en riesgo su disponibilidad y aumentando sus precios']
            random_dato = random.choice(datos)
            await ctx.send(f'{random_dato}')
        else:
            await ctx.send("Si deseas un dato más tarde, avisame.")

    except Exception as e:
        await ctx.send("No recibí una respuesta a tiempo")
        print(f"Error:{e}")

@final_bot.command()
async def causa(ctx):
    await ctx.send("¿Deseas saber las causas del cambio climático?(si o no)")
    def verificar3(m):   #función para asegurarse de que el mensaje sea del mismo autor que ejecutó el comando
        return ctx.author == m.author

    try:
        respuesta_causa = await final_bot.wait_for('message',check = verificar3, timeout = 15) # espera 15 segundos por la respuesta
        dato3 = respuesta_causa.content
        dato3 = dato3.lower()
        if dato3 == "si":
            causas = ['El uso excesivo de enrgía','El uso excesivo del transporte','La ganadería intensiva','La tala de bosques','La quema de combustibles fósiles']
            random_causa = random.choice(causas)
            await ctx.send(f'Una de las causas es: {random_causa}')
        else:
            await ctx.send("Si deseas saber alguna causa más tarde, avisame.")

    except Exception as e:
        await ctx.send("No recibí una respuesta a tiempo")
        print(f"Error:{e}")

@final_bot.command()
async def consecuencia(ctx):
    await ctx.send("¿Deseas saber las consecuencias del cambio climático?(si o no)")
    def verificar4(m):   #función para asegurarse de que el mensaje sea del mismo autor que ejecutó el comando
        return ctx.author == m.author

    try:
        respuesta_consecuencia = await final_bot.wait_for('message',check = verificar4, timeout = 15) # espera 15 segundos por la respuesta
        dato4 = respuesta_consecuencia.content
        dato4 = dato4.lower()
        if dato4 == "si":
            consecuencias = ['Escasez de alimentos','Desaparición de especies','Aumento del nivel del océano y calentamiento del agua','Fenómenos extremos más frecuentes','Elevación de las temperaturas','Problemas de salud','Pérdidas económicas','Daños a infraestructuras']
            random_consecuencia = random.choice(consecuencias)
            await ctx.send(f'Una de las consecuencias es: {random_consecuencia}')
        else:
            await ctx.send("Si deseas saber alguna consecuencia más tarde, avisame.")

    except Exception as e:
        await ctx.send("No recibí una respuesta a tiempo")
        print(f"Error:{e}")

# Token de servidor de DISCORD
final_bot.run("")