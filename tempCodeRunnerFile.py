while b < a:
    letters = string.ascii_letters + string.digits
    f = open("Nitro.txt", "a")
    f.write('https://discord.gift/' + ''.join(random.choice(letters) for i in range(16)) + '\n')
    print('\u001b[32mhttps://discord.gift/' + ''.join(random.choice(letters) for i in range(16)) + '\u001b[37m')
    b += 1