def frequency():
    Spos = int(input("Enter the Speed of sound:"))
    WaveLength = float(input("Enter the WaveLength:"))

    WaveL = WaveLength / 100

    Frequency = Spos / WaveLength

    Total = Spos * 1000 / 15

    print("Freqency of Sound is :", str(Total))

frequency()
