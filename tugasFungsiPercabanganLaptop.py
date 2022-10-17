# buat progra, fungsi percabangan mengenai kondisi pemilihan jenis laptop


def belilaptop():
    print("""
laptop yang tersedia:
lenovo, macbook,dell, acer, asus,hp
    
    """)
    jenislaptop = input("laptop yang ingin kamu beli: ")

    if jenislaptop == "lenovo":

        merkLenovo = input(
            """
1. Ideapad slim 3
2. Ideapad slim 5
3. Ideapad Flex 5
4. Ideapad Legion 5 pro
5. Thinkpad 
masukkan angka: """
        )
        if merkLenovo == "1":
            print(
                """
harga: 5.417.800
spesifikasi:
sistem operasi: windows
Prosessor: Intel core 13 gen 10
penyimpanan: 256GB SSDRAM: 8GB

                  """
            )
        elif merkLenovo == "2":
            print(
                """
harga: 10.000.000
spesifikasi:
sistem operasi: windows
Prosessor: Intel core 15 gen 11
penyimpanan 512GB SSD
RAM: 8GB
                  """
            )
        elif merkLenovo == "3":
            print(
                """
harga: 13.000.000
spesifikasi:
sistem operasi: windows
Prosessor: Intel core 17 gen 11
penyimpanan 512GB SSD
RAM: 8GB
                  """
            )
        elif merkLenovo == "4":
            print(
                """
harga: 5.000.000
spesifikasi:
sistem operasi: windows
Prosessor: Intel core 15 gen 8
penyimpanan 256GB SSD
RAM: 4GB
                  """
            )
        elif merkLenovo == "5":
            print(
                """
harga: 7.000.000
spesifikasi:
sistem operasi: windows
Prosessor: Intel core 13 gen 1
penyimpanan 512GB SSD
RAM: 8GB
                  """
            )

    elif jenislaptop == "macbook":
        merkMacbook = input(
            """
1. Apple macbook pro 2022(M2)
2. Apple macbook pro 2021(M1 pro/M1 Max)
3. Apple MacBook Air 2020 M1
4. Apple MacBook Pro 2019 16 i7
5. Apple MacBook Pro 2018 Touch Bar
masukkan angka: """
        )
        if merkMacbook == "1":
            print(
                """
harga: 21.999.000
spesifikasi:
Prosessor: M2
penyimpanan 256GB SSD
RAM: 8GB

                  """
            )
        elif merkMacbook == "2":
            print(
                """
harga: 26.490.000
spesifikasi:
Prosessor: M1
penyimpanan 512GB SSD
RAM: 16GB
                  """
            )
        elif merkMacbook == "3":
            print(
                """
harga: 17200000
spesifikasi:
Prosessor: M1 2020
penyimpanan: 256GB SSD
RAM: 8GB
                  """
            )
        elif merkMacbook == "4":
            print(
                """
harga: 15000000
spesifikasi:
Prosessor: Intel core 15 gen 10
penyimpanan 256GB SSD
RAM: 8GB
                  """
            )
        elif merkMacbook == "5":
            print(
                """
harga: 12.000.000
spesifikasi:
Prosessor: Intel core 13 gen 10
penyimpanan 256GB SSD
RAM: 8GB
                  """
            )
    elif jenislaptop == "acer":
        merkAcer = input(
            """
1. Aspire 3 slim (A314-35)
2. Acer Aspire E5-471
3. Acer Aspire E5-471-36WV
4. ACER Aspire E5-473G-5500U
5. ACER Aspire R7-372T


masukkan angka: """
        )
        if merkAcer == "1":
            print(
                """
harga: 4500000
spesifikasi:
Prosessor: Intel Celeron N5100 quad-core
penyimpanan 256GB SSD
RAM: 8GB

                    """
            )
        elif merkAcer == "2":
            print(
                """
harga: 4800000
spesifikasi:
Prosessor: Intel core i3 4005U
penyimpanan 500GB HDD
RAM: 2GB
                    """
            )

        elif merkAcer == "3":
            print(
                """
harga: 4900000
spesifikasi:
Prosessor: Intel core i3 4030U
penyimpanan 500GB SSD
RAM: 2GB
                    """
            )
        elif merkAcer == "4":
            print(
                """
harga: 9600000
spesifikasi:
Prosessor: Intel Core i7 5500U
penyimpanan 1TB HDD
RAM: 4GB
                    """
            )
        elif merkAcer == "5":
            print(
                """
harga: 17.999.000
spesifikasi:
Prosessor: Intel core i3 6500U
penyimpanan 512GB SSD
RAM: 8GB
                    """
            )

    elif jenislaptop == "dell":

        merkDell = input(
            """
1. Dell Inspiron 13 5370
2. Dell Inspiron 14 5482 Touch Screen
3. Dell Inspiron 14 5491 2 in 1
4. Dell Inspiron 15 3576
5. Dell Inspiron 14 7472


masukkan angka: """
        )
        if merkDell == "1":
            print(
                """
harga: 8170000
spesifikasi:
Prosessor: Intel Core i3-8130U
penyimpanan 256GB SSD
RAM: 8GB

                    """
            )
        elif merkDell == "2":
            print(
                """
harga: 8820000
spesifikasi:
Prosessor: Intel Core i3-8145U
penyimpanan 256GB SSD
RAM: 4GB
                    """
            )

        elif merkDell == "3":
            print(
                """
harga: 13450000
spesifikasi:
Prosessor: Intel Core i5-10210U
penyimpanan: SSD 512GB
RAM: 8GB
                    """
            )
        elif merkDell == "4":
            print(
                """
harga: 7020000
spesifikasi:
Prosessor: Intel Core i3-7020U
penyimpanan 1TB HDD
RAM: 4GB
                    """
            )
        elif merkDell == "5":
            print(
                """
harga: 11.850.000
spesifikasi:

Prosessor: Intel Core i5-8250U
VGA: nVidia GeForce MX150 2GB
penyimpanan 256GB SSD
RAM: 8GB
                    """
            )

    elif jenislaptop == "hp":
        merkHp = input(
            """
1. HP Pavilion X360 13-U182TU
2. HP Pavilion X360 14-CD1042TX
3. HP Pavilion 13-AN0014TU
4. HP ENVY X360 13-AR0108AU
5. HP ENVY 13-AQ1018TX


masukkan angka: """
        )
        if merkHp == "1":
            print(
                """
harga: 7800000
spesifikasi:
Prosessor: Intel Core i3-7100U
penyimpanan 256GB SSD
RAM: 4GB

                    """
            )
        elif merkHp == "2":
            print(
                """
harga: 14800000
spesifikasi:
Prosessor: Intel Core i7-8565U
penyimpanan: 1TB HDD + SSD 128 GB
RAM: 8 GB DDR4
                    """
            )

        elif merkHp == "3":
            print(
                """
harga: 14700000
spesifikasi:
Prosessor: Intel Core i7-8565U
penyimpanan: SSD 512GB
RAM: 8GB
                    """
            )
        elif merkHp == "4":
            print(
                """
harga: 17500000
spesifikasi:
Prosessor: AMD Ryzen 7 3700U
penyimpanan: 512GB SSD
RAM: 16GB
                    """
            )
        elif merkHp == "5":
            print(
                """
harga: 18900000

spesifikasi:
Prosessor: Intel Core i5-8250U
VGA: nVidia GeForce MX250
penyimpanan 512GB SSD
RAM: 16GB DDR4
                    """
            )
            
    elif jenislaptop == "asus":
        merkAsus = input(
            """
1. Asus Zenbook 14X OLED
2. Asus Vivobook Pro 15 OLED
3. Asus Vivobook Pro 14 OLED K3400
4. Asus VivoBook Ultra 15 OLED K513
5. Asus ExpertBook B5 Flip


masukkan angka: """
        )
        if merkAsus == "1":
            print(
                """
harga: 24000000
spesifikasi:
Prosessor: Intel Core 7 Gen 11
VGA: NVIDIA GeForce MX450
penyimpanan 1 TB PCIe SSD
RAM: 16GB LPDDR4X

                    """
            )
        elif merkAsus == "2":
            print(
                """
harga: 17499000
spesifikasi:
Prosessor: AMD Ryzen 5000
VGA: NVIDIA GeForce RTX 3050
penyimpanan: 1TB HDD + SSD 128 GB
RAM: 16 GB LPDDR4
                    """
            )

        elif merkAsus == "3":
            print(
                """
harga: 14599000
spesifikasi:
Prosessor: Intel Core i5 gen 11
penyimpanan: SSD 512GB
RAM: 8GB
                    """
            )
        elif merkAsus == "4":
            print(
                """
harga: 8.599.000
spesifikasi:
Prosessor: Intel Core i5 Gen 11
penyimpanan: 256GB SSD
RAM: 4GB
                    """
            )
        elif merkAsus == "5":
            print(
                """
harga: 15771000

spesifikasi:
Prosessor: Intel Core i7-1165G7 Gen 11
VGA: nVidia GeForce MX250
penyimpanan 1TB SSD
RAM: 16GB DDR4
                    """
            )

    else:
        print("laptop yang kamu inputkan salah")


belilaptop()
