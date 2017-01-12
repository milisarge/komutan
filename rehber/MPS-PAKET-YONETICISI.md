MPS (Milis Paket Sistemi)

Mps Milis işletim sisteminin kendine özgü sıfırdan bash betik dilinde yazılmış paket yöneticisidir.
Mps ile talimatnamedeki talimatları kullanarak paket üretebilir,paket kurabilir kaldırabilir ve güncelleyebilirsiniz.

mps -G					ikili paket veritabanini gunceller

mps -Ggit				git sunucusundan talimatname ve sistem gunceller

mps -kur   paket_ismi	ilgili paketi bagimliliklariyla agdan cekip kurar

mps -s     paket_ismi	ilgili paketi kaldirir

mps -k     paket_ismi	yereldeki paketi bagimliliksiz kurar

mps -kl					kurulu paket listesini verir

mps -kk    paket_ismi	ilgili paketin kurulu olma durumunu verir

mps -d     paket_ismi	ilgili paketin talimat dosyasına göre sadece derler,paketler

mps -derle paket_ismi	ilgili paketin talimat dosyasına göre bagimliliklariyla beraber derler,paketler ve kurar.
