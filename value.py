from conn import *

#=========================== Array ==============
array_keriteria = [['kecerdasan'],['kinerja'],['perilaku']]
array_sikap = [
['common sense','1'],
['ide','1'],
['berfikir','1'],
['penalaraan','1'],
['konsentrsi','1'],
['logika','1'],
['fleksibel','1'],
['imajinasi','1'],
['antisipasi','1'],
['potensi kecerdasan','1'],
['energi','2'],
['ketelitian','2'],
['kehati-hatian','2'],
['EQ','2'],
['dorongan berprestasi','2'],
['perencanaan','2'],
['kekuasaan','3'],
['pengaruh','3'],
['keteguhan hati','3'],
['pemenuhan','3']
]

# q.executemany('INSERT INTO `keriteria` VALUES (NULL, %s);',array_keriteria)
# conn.commit()

# q.executemany('INSERT INTO `sikap` VALUES (NULL, %s, %s);',array_sikap)
# conn.commit()