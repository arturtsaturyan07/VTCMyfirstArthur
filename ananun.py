import wave
import struct

source = wave.open("instasamka.wav", mode="rb")
dest = wave.open("out.wav", mode="wb")

dest.setparams(source.getparams())

# գտնենք ֆրեյմների քանակը
frames_count = source.getnframes()

data = struct.unpack("<" + str(frames_count) + "h",
                     source.readframes(frames_count))

# սա ծրագրի հիմնական տողն է, որը շրջում է ցուցակը
newdata = data[::-1]

newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

# պարունակությունը գրում ենք ձևափոխված ֆայլում:
dest.writeframes(newframes)
source.close()
dest.close()