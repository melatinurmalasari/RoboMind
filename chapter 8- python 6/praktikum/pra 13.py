nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	        {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def skorakhir (mid,uas):
    skor = (mid + (2 * uas)) / 3
    return skor

def ttinggi (data):
    nilai2 = []
    for i in range(len(data)):
        List = (data[i])
        nilai = skorakhir(List['mid'],List['uas'])
        nilai2 += [nilai]
        skorfinal = nilai2[0]
        for ttinggi in nilai2:
            if(ttinggi > skorfinal):
                skorfinal = ttinggi
            else:
                continue

        if(skorfinal == nilai):
            nim = List['nim']
            nama = List['nama']
        else:
            continue

    skor = print('Nilai paling tinggi diperoleh oleh :', nim , '/', nama)
    return skor

ttinggi(nilaiMhs)