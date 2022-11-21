from encoder import encoder
from decoder import decoder
from copier import copy_to_file

encoder_file = 'encoder.txt'
decoder_file = 'decoder.txt'


txt_enc = encoder(input('Введите текст для сжатия: '))
copy_to_file(encoder_file, txt_enc)

txt_dec = decoder(txt_enc)
copy_to_file(decoder_file, txt_dec)
