'''
Започнах да програмирам съвсем случайно.
Завършила съм ПМГ без никакво намерение да програмирам.
Влязох във ФМИ съвсем случайно, напук на нашите, за да им покажа, че мога.
Python e езика, на който основно пиша, а той като език от високо ниво
 ме оставя мен с доста бегли познания за същността на нещата.
Алгортими не съм учила във ФМИ, но ги намирам за изключително полезни.
Имам желание да разбирам нещата, затова желая да посещавам курса.
Очакванията ми са в очакване, понеже Ванката е стабилен.
'''


def decodeMessage(string):

    string = string[len(string)/2:] + string[:len(string)/2]
    parts = string.split("~")

    lenAlpha = int(parts[0])
    lenKey = int(parts[2])
    alpha = parts[1][:lenAlpha]
    encr = parts[1][lenAlpha:-lenKey]
    key = parts[1][-lenKey:]
    indexes_encr = [alpha.index(x) for x in encr]
    encr_len = len(encr)
    mer = encr_len/len(key) + 1
    key_expanded = key * mer
    key_expanded = key_expanded[:encr_len]
    indexes_k = [alpha.index(x) for x in key_expanded]
    indexes_message = []
    alpha_len = len(alpha)

    for i in range(encr_len):
        eachIndex = indexes_encr[i] - indexes_k[i]
        if eachIndex >= 0:
            indexes_message.append(eachIndex)
        else:
            indexes_message.append(eachIndex + alpha_len)

    message_list = [alpha[i] for i in indexes_message]
    message = ''.join(message_list)
    print(message)


hack = "TJKUMbUUJTIREuKOXD'HR.sTOVSWU!KSJ(O.sVYtWZTTZVULsNOBdYONXFsvEu(PgWJsRTSVsYKOfDZOJSNVWu(IU!yAaMs?OW.tYaVET.A IQXTMQURJ.HLs'VHa'OTYUSzCQ!SePzsuMTzYQ!SM!NOdOH SuPMa)yA!LsKOPEUM,VAaMs.SuKOkDJEcIIStHACKBULGARIA~1260~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .',!?()rEPNtg,yTYMsJOFOtkZ sd EKsVYtXPIOUMs HK't(PYSROEAsq.JfPyAJ HVRVCUYaZsPITzMQ'UMZTEJXANEBCUYWRI!Os.Su(IkD!OdADLCKNFXDZOJ THRVCQdZMRRUMPNIDtISGTJQSz"
ex1 = "rc hscesi tcrest~410~thisaecr .rcese"
ex2 = "fl k.ccfsIolskv.~312~ .Ifrckslovelvo"
ex3 = "o?uin uw?stutnfwat?~413~orwa? thfuisnnrsiu"
decodeMessage(hack)

'''
decodeMessage(ex1)
decodeMessage(ex2)
decodeMessage(ex3)
'''
