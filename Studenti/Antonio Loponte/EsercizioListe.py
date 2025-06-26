eta_studenti = [20, 22, 19, 21, 23, 20, 22, 19]

media_eta = 0


for eta_media in eta_studenti:
    media_eta += eta_media


media_eta /= len(eta_studenti)


print(f"La media delle età degli studenti è: {media_eta}")


eta_studenti.sort(reverse=True)

print(f"L'età più alta è: {eta_studenti[0]}")



