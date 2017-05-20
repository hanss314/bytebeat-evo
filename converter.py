import wave, struct

reader = wave.open('ballade1.wav','rb')

for i in range(reader.getnframes()):
	print(
		
			int(
				struct.unpack(
					'B',reader.readframes(1)
				)[0]
			)
		
	)