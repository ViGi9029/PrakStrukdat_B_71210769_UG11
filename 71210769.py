class RakBuku:
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size
    
    def getHash(self,key):
        sum = 0
        for char in key:
            sum += ord(char) # mendapatkan nilai ASCII
        return sum % self.size

    def probing(self, key):
        for index in range(self.size):
            # probeHash = (self._getHash(key)+index) % self.size
            probeHash = self.linearProbing(key, index)
            # valid bila index adalah None atau ber-flag deleted
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash

    
    def linearProbing(self, key, index):
        return (self.getHash(key)+index) % self.size

        # menambahkan key pada hash table
    def tambahBuku(self, jenisBuku, namaBuku):
        # periksa apakah key_hash sudah terpakai
        hash_key = self.getHash(jenisBuku)
        # buat pasangan key value
        key_value = [jenisBuku, namaBuku]
 
        if self.map[hash_key] is None:
            self.map[hash_key] = list([key_value])
            return True
        else:
            hash_key = self.probing(jenisBuku)
            if hash_key is None:
                print("Rak Buku anda sudah penuh")
                return False
            else:
                self.map[hash_key] = list([key_value])
                return True

    def ambilBuku(self,jenisBuku):
        hash_key = self.getHash(jenisBuku)
        if self.map[hash_key] is None:
            return False    
        else:
            for index in range(self.size):
                hash_key = self.linearProbing(jenisBuku,index)
                if self.map[hash_key][0][0] == jenisBuku:
                    print("deleting",jenisBuku)
                    self.map[hash_key] = 'deleted'
                    return True
            print('key',jenisBuku,'tidak ditemukan')
            return False
    
    def lihatBuku(self, jenisBuku):
        hash_key = self.getHash(jenisBuku)
        if self.map[hash_key] is not None and self.map[hash_key]!= 'deleted':
            for index in range(self.size):
                hash_key = self.linearProbing(jenisBuku, index)
                if(self.map[hash_key][0][0] == jenisBuku):
                    return self.map[hash_key][0][1]
        print("Key",jenisBuku, "tidak ditemukan")
        return "None"
    
    def printAll(self):
        print('='*25,'List Buku','='*25)
        for item in self.map:
            if item is not None and item != 'deleted':
                print("Nama :",item[0][1],"<>","Jenis :",item[0][0])
        print('='*50)

if __name__ == "__main__":
    rak1 = RakBuku()
    rak1.tambahBuku("History", "Mein Kampf (B01)")
    rak1.tambahBuku("Fantasy", "The Witcher (B02)")
    rak1.tambahBuku("Mystery", "Exile (B03)")
    rak1.tambahBuku("Sci Fi", "The Martian (B04)")
    rak1.tambahBuku("History", "World War (B05)")
    rak1.tambahBuku("Romance", "Twilight (B06)")
    print(rak1.lihatBuku("History"))
    print(rak1.lihatBuku("Romance"))
    rak1.ambilBuku("Sci Fi")
    rak1.ambilBuku("Romance")
    rak1.printAll()