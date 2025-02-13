// testando
#Criando o Perfil do Aço
print("Bem Vindo(a) ao S77eel\n")
print("Para iniciarmos o dimensionamento devemos adotar um perfil a ser utilizado com base na Tabela de Perfis Laminados I e H\n")

print(
    "Escolha um perfil fornecido pelo programa ou informe os dados de um novo perfil:\n"
    "(1) Perfil W 150 x 13.0\n"
    "(2) Perfil W 250 x 17.9\n"
    "(3) Perfil W 310 x 21.0\n"
    "(4) Novo Perfil\n")

while True:
    perfil = int(input("Digite o número da opção desejada: "))

    if perfil == 1:
        arquivo = open ('Perfil W150x13.0.txt', 'w\n')
        arquivo.write('Massa Linear = 13.0Kg/m\n')
        arquivo.write('Largura (d) = 148mm\n')
        arquivo.write('Largura da aba (bf) = 100mm\n')
        arquivo.write('Espessura da alma (tw) = 4.3mm\n')
        arquivo.write('Espessura da aba (tf) = 4.9mm\n')
        arquivo.write('Altura Interna (h) = 138mm\n')
        arquivo.write('Altura livre da Alma (d´) = 118mm\n')
        arquivo.write('Área = 16.6cm2\n')
        arquivo.write('Eixo X-X\n')
        arquivo.write('Inércia em X (Ix) = 635cm4\n')
        arquivo.write('Wx = 85.8cm3\n')
        arquivo.write('rx = 6.18cm\n')
        arquivo.write('Zx = 96.4cm3\n')
        arquivo.write('Eixo Y-Y\n')
        arquivo.write('Inércia em Y (Iy) = 82cm4\n')
        arquivo.write('Wy = 16.4cm3\n')
        arquivo.write('ry = 2.22cm\n')
        arquivo.write('Zy = 25.5cm3\n')
        arquivo.write('rt = 2.60cm\n')
        arquivo.write('It = 1.72cm4\n')
        arquivo.write('Esbeltez\n')
        arquivo.write('Aba - If (bf/2tf) = 10.20\n')
        arquivo.write('Alma - Iw (d´/tw) = 27.49\n')
        arquivo.write('Cw = 4181cm6\n')
        arquivo.write('u = 0.67m2/m\n')
        arquivo.close()
        arquivo = open('Perfil W150x13.0.txt', 'r')
        print("Abaixo temos informações sobre o perfil adotado: W 150 x 13.0")
        print(arquivo.read())
        umpp = 13.0
        umlargura = 148
        umbf= 100
        umtw = 4.3
        umtf = 4.9
        umh = 138
        umdlinha = 118
        umarea = 16.6
        umix = 635
        umwx = 85.8
        umrx = 6.18
        umzx = 96.4
        umiy = 82
        umwy = 16.4
        umry = 2.22
        umzy = 25.5
        umrt = 2.60
        umit = 1.72
        umbf2tf = 10.20
        umdlinhatw = 27.49
        umcw = 4181
        umu = 0.67
        arquivo.close()
        break
        
    elif perfil ==2:
        arquivo = open ('Perfil W250x17.9.txt', 'w\n')
        arquivo.write('Massa Linear = 17.9Kg/m\n')
        arquivo.write('Largura (d) = 251mm\n')
        arquivo.write('Largura da aba (bf) = 101mm\n')
        arquivo.write('Espessura da alma (tw) = 4.8mm\n')
        arquivo.write('Espessura da aba (tf) = 5.3mm\n')
        arquivo.write('Altura Interna (h) = 240mm\n')
        arquivo.write('Altura livre da Alma (d´) = 220mm\n')
        arquivo.write('Área = 23.1cm2\n')
        arquivo.write('Eixo X-X\n')
        arquivo.write('Inércia em X (Ix) = 2291cm4\n')
        arquivo.write('Wx = 182.6cm3\n')
        arquivo.write('rx = 9.96cm\n')
        arquivo.write('Zx = 211.0cm3\n')
        arquivo.write('Eixo Y-Y\n')
        arquivo.write('Inércia em Y (Iy) = 91cm4\n')
        arquivo.write('Wy = 18.1cm3\n')
        arquivo.write('ry = 1.99cm\n')
        arquivo.write('Zy = 28.8cm3\n')
        arquivo.write('rt = 2.48cm\n')
        arquivo.write('It = 2.54cm4\n')
        arquivo.write('Esbeltez\n')
        arquivo.write('Aba - If (bf/2tf) = 9.53\n')
        arquivo.write('Alma - Iw (d´/tw) = 45.92\n')
        arquivo.write('Cw = 13735cm6\n')
        arquivo.write('u = 0.88m2/m\n')
        arquivo.close()
        arquivo = open('Perfil W250x17.9.txt', 'r')
        print("Abaixo temos informações sobre o perfil adotado: W 250 x 17.9")
        print(arquivo.read())
        dopp = 17.9
        dolargura = 251
        dobf = 101
        dotw = 4.8
        dotf = 5.3
        doh = 240
        dodlinha = 220
        doarea = 23.1
        doix = 2291
        dowx = 182.6
        dorx = 9.96
        dozx = 211.0
        doiy = 91
        dowy = 18.1
        dory = 1.99
        dozy = 28.8
        dort = 2.48
        doit = 2.54
        dobf2tf = 9.53
        dodlinhatw = 45.92
        docw = 13735
        dou = 0.88
        arquivo.close()
        break
        
    elif perfil ==3:
        arquivo = open ('Perfil W310x115.0.txt', 'w\n')
        arquivo.write('Massa Linear = 21.0Kg/m\n')
        arquivo.write('Largura (d) = 303mm\n')
        arquivo.write('Largura da aba (bf) = 101mm\n')
        arquivo.write('Espessura da alma (tw) = 5.1mm\n')
        arquivo.write('Espessura da aba (tf) = 5.7mm\n')
        arquivo.write('Altura Interna (h) = 292mm\n')
        arquivo.write('Altura livre da Alma (d´) = 272mm\n')
        arquivo.write('Área = 27.2cm2\n')
        arquivo.write('Eixo X-X\n')
        arquivo.write('Inércia em X (Ix) = 3776cm4\n')
        arquivo.write('Wx = 249.2cm3\n')
        arquivo.write('rx = 11.77cm\n')
        arquivo.write('Zx = 291.9cm3\n')
        arquivo.write('Eixo Y-Y\n')
        arquivo.write('Inércia em Y (Iy) = 98cm4\n')
        arquivo.write('Wy = 19.5cm3\n')
        arquivo.write('ry = 1.90cm\n')
        arquivo.write('Zy = 31.4cm3\n')
        arquivo.write('rt = 2.42cm\n')
        arquivo.write('It = 3.27cm4\n')
        arquivo.write('Esbeltez\n')
        arquivo.write('Aba - If (bf/2tf) = 8.86\n')
        arquivo.write('Alma - Iw (d´/tw) = 53.25\n')
        arquivo.write('Cw = 21628cm6\n')
        arquivo.write('u = 0.98m2/m\n')
        arquivo.close()
        arquivo = open('Perfil W310x115.0.txt', 'r')
        print("Abaixo temos informações sobre o perfil adotado: W 310 x 21.0")
        print(arquivo.read())
        trpp = 21.0
        trlargura = 303
        trbf = 101
        trtw = 5.1
        trtf = 5.7
        trh = 292
        trdlinha = 272
        trarea = 27.2
        trix = 3776
        trwx = 249.2
        trrx = 11.77
        trzx = 291.9
        triy = 98
        trwy = 19.5
        trry = 1.90
        trzy = 31.4
        trrt = 2.42
        trit = 3.27
        trbf2tf = 8.86
        trdlinhatw = 53.25
        trcw = 21628
        tru = 0.98
        arquivo.close()
        break
        
    elif perfil ==4:
        print("Com base na Tabela de Perfil Laminado I e H e Perfil Soldado, digite abaixo os valores do Perfil:")
        print("Se a Tabela não possuir algum valor, digite 0 (Zero)")
        print("Utilize o ponto para as casas decimais")
        arquivo = (input("Digite o nome do perfil (Da seguinte maneira: LL NNN x NN.N): "))
        qpp = float(input("Digite a Massa Linear (unidade Kg/m): "))
        qlargura = float(input("Digite a Largura (d)(unidade mm): "))
        qbf = float(input("Digite a Largura da aba (bf)(munidade mm): "))
        qtw = float(input("Digite a Espessura da alma (tw) (unidade mm): "))
        qtf = float(input("Digite a Espessura da aba (tf) (unidade mm): "))
        qh = float(input("Digite a Altura Interna (h) (unidade mm): "))
        qdlinha = float(input("Digite a Altura livre da Alma (d´) (unidade mm): "))
        qarea = float(input("Digite a Área (unidade cm2): "))
        qix = float(input("Digite a Inércia em X (Ix) (unidade cm4): "))
        qwx = float(input("Digite o valor de Wx (unidade cm3): "))
        qrx = float(input("Digite o valor de rx (unidade cm): "))
        qzx = float(input("Digite o valor de Zx (unidade cm3): "))
        qiy = float(input("Digite a Inércia em Y (Iy) (unidade cm4): "))
        qwy = float(input("Digite o valor de Wy (unidade cm3): "))
        qry = float(input("Digite o valor de ry (unidade cm): "))
        qzy = float(input("Digite o valor de Zy (unidade cm3): "))
        qrt = float(input("Digite o valor de rt (unidade cm): "))
        qit = float(input("Digite o valor de It (unidade cm4): "))
        qbf2tf = float(input("Digite o valor da Esbeltez na Aba - If (bf/2tf): "))
        qdlinhatw = float(input("Digite o valor da Esbeltez Alma - Iw (d´/tw): "))
        qcw = float(input("Digite o valor de Cw (unidade cm6): "))
        qu = float(input("Digite o valor de u (unidade m2/m): "))
        break

    else:
        print("Perfil não encontrado. Tente Novamente")
    
if perfil == 1:
    pp = umpp
    largura = umlargura
    bf = umbf
    tw = umtw 
    tf= umtf
    h= umh 
    dlinha = umdlinha 
    area= umarea 
    ix = umix 
    wx = umwx 
    rx = umrx 
    zx= umzx
    iy = umiy 
    wy = umwy 
    ry = umry
    zy = umzy 
    rt = umrt 
    it = umit 
    bf2tf = umbf2tf 
    dlinhatw = umdlinhatw
    cw = umcw 
    u = umu

elif perfil == 2:
    pp = dopp
    largura = dolargura
    bf = dobf
    tw = dotw 
    tf= dotf
    h= doh 
    dlinha = dodlinha 
    area= doarea 
    ix = doix 
    wx = dowx 
    rx = dorx 
    zx= dozx
    iy = doiy 
    wy = dowy 
    ry = dory
    zy = dozy 
    rt = dort 
    it = doit 
    bf2tf = dobf2tf 
    dlinhatw = dodlinhatw
    cw = docw 
    u = dou

elif perfil == 3:
    pp = trpp
    largura = trlargura
    bf = trbf
    tw = trtw 
    tf= trtf
    h= trh 
    dlinha = trdlinha 
    area= trarea 
    ix = trix 
    wx = trwx 
    rx = trrx 
    zx= trzx
    iy = triy 
    wy = trwy 
    ry = trry
    zy = trzy 
    rt = trrt 
    it = trit 
    bf2tf = trbf2tf 
    dlinhatw = trdlinhatw
    cw = trcw 
    u = tru
    
elif perfil == 4:
    pp = qpp
    largura = qlargura
    bf = qbf
    tw = qtw 
    tf= qtf
    h= qh 
    dlinha = qdlinha 
    area= qarea 
    ix = qix 
    wx = qwx 
    rx = qrx 
    zx= qzx
    iy = qiy 
    wy = qwy 
    ry = qry
    zy = qzy 
    rt = qrt 
    it = qit 
    bf2tf = qbf2tf 
    dlinhatw = qdlinhatw
    cw = qcw 
    u = qu
    
#PESOS ATUANTES NA VIGA DE AÇO
print(
    "\nDigite as informações da viga em Aço\n"
      "Utilize o ponto para as casas decimais\n"
      "Digite os pesos atuantes na viga:\n"
      )

pesop = pp/100
larg = largura/1000
wall = float(input("Digite o peso da parede sobre a viga (kN/m): "))
laje = float(input("Digite o peso da laje sobre a viga (kN/m): "))
carga_acidental = float(input("Digite a carga acidental sobre a viga (kN/m): "))
comprimento = float(input("Digite o comprimento da viga (m): "))
if carga_acidental >= 1:
    momento = float(input("Digite a distância do ponto da carga acidental em relação ao ponto 0 da viga (m): "))
print()
print("A carga total será de: ",pesop+wall+laje+carga_acidental,"kN/m")
print("A viga tem", comprimento," metros de comprimento")
print("A viga tem", larg," metros de largura")
print("A viga tem", area," centímetros quadrados de área")
print()

#CALCULO DO MOMENTO RESISTENTE
#Flambagem Local
print("Escolha a tipologia do aço: ")
print("Digite 1 para aço MR250")
print("Digite 2 para aço AR350")
tabela = int(input("Digite o número referente ao tipo de aço: "))

#Para Aço MR350
if tabela == 1:
    mesa_lamb_p = 10.7
    mesa_lamb_r = 28
    alma_lamb_p = 106
    alma_lamb_r = 161
    fy = 25
#Para Aço AR350
elif tabela == 2:
    mesa_lamb_p = 9.1
    mesa_lamb_r = 24
    alma_lamb_p = 90
    alma_lamb_r = 136
    fy = 35
print()

#Para Mesa
multi_tf = 2*tf
lamb_b_mesa = bf/multi_tf
if lamb_b_mesa < mesa_lamb_p:
    secao_mesa = 1
    print ("Mesa de seção Compacta")
    print()
elif mesa_lamb_p < lamb_b_mesa < mesa_lamb_r:
    secao_mesa = 2
    print ("Mesa de seção Semicompacta")
    print()
elif lamb_b_mesa > mesa_lamb_r:
    secao_mesa = 3
    print ("Mesa de seção Esbelta")
    print()
    
#Para Alma
lamb_b_alma = h/tw
if lamb_b_alma < alma_lamb_p:
    secao_alma = 1
    print ("Alma de seção Compacta")
    print()
elif alma_lamb_p < lamb_b_alma < alma_lamb_r:
    secao_alma = 2
    print ("Alma de seção Semicompacta")
    print()
elif lamb_b_alma > alma_lamb_r:
    secao_alma = 3
    print ("Alma de seção Esbelta")
    print()
#Para seção Compacta
if secao_mesa == 1:
    if secao_alma == 1:
        print("Para viga de Mesa e Alma de Seção Compacta")
        mp = zx*fy
        print()
        print("Mp desta viga é igual a", mp,"kN.cm")
        md = mp//1.1
        print("Md desta viga é igual a", md,"kN.cm")
        print()
        
        #Viga Curta
        print ("Verificação se a viga é considerada Curta: ")
        lb = float(input("Digite o valor de Lb (cm): "))
        iy_curta = ry
        E = float(input("Digite o valor de E(kN/cm2): "))
        fy_short = fy
        import math
        num = E/fy_short
        raiz = math.sqrt(num)
        lbp = 1.76*iy_curta*raiz
        print("O valor de Lbp é", lbp,"cm")
        if  lb > lbp:
            print("Portanto a viga não é considerada curta.")
            print()

            #Viga Longa
            print ("Verificação se a viga é considerada Longa: ")
            teta_r = fy*0.3
            print("O valor de σr é:", teta_r)
            j = float(input("Digite o valor de J: "))
            print()
            fy_longa = fy
            subtracao_b1 = fy_longa-teta_r
            multiplicacao_b1 = subtracao_b1*wx
            multiplicacao_b2 = E*j
            valor_b1 = multiplicacao_b1/multiplicacao_b2
            print("B1 =", valor_b1,)
            print()
            if cw == 0:
                iy_lbr = iy
                pot_cw = h**2
                multiplicacao_cw = pot_cw*iy_lbr
                cw_longa = multiplicacao_cw/4
                print("Cw =", cw_longa,)
                print()
            else:
                cw_longa = cw
                print("Cw =", cw_longa,)
                print()
            #Fómulas
            iy_lbr = iy
            pot_lbr = valor_b1**2
            multiplicacao_lbr = 27*cw_longa*pot_lbr
            div_raiz1 = multiplicacao_lbr/iy
            mais_raiz_1 = 1+div_raiz1
            import math
            raiz_lbr_1 = math.sqrt(mais_raiz_1)
            mais_raiz_2 = 1+raiz_lbr_1
            import math
            raiz_lbr_2 = math.sqrt(mais_raiz_2)
            multiplicacao_1 = iy_lbr*j
            import math
            raiz_lbr_3 = math.sqrt(multiplicacao_1)
            multiplicacao_2 = 1.38*raiz_lbr_3
            multiplicacao_3 = j*valor_b1
            div_lbr_1 = multiplicacao_2/multiplicacao_3
            lbr = div_lbr_1*raiz_lbr_2
            print("O valor de Lbr é", lbr,"cm")
            if  lb < lbr:
                print("Portanto a viga não é considerada longa.")
                print()

                #Viga Intermediária
                print ("Sendo assim, tem-se uma viga Intermediária: ")
                fy_inter = fy
                mp_inter = zx*fy_inter
                print()
                print("Valor de Mp =", mp_inter,)
                subtracao_inter = fy_inter-teta_r
                mr_inter = wx*subtracao_inter
                print("Valor de Mr =", mr_inter,)
                print()
                cb = 1.14
                print("Cb =", cb,)
                sub_mn_1 = lb-lbp
                sub_mn_2 = lbr-lbp
                div_subs = sub_mn_1/sub_mn_2
                sub_mn_3 = mp_inter-mr_inter
                multiplicacao_mn_1 = sub_mn_3*div_subs
                sub_mn_4 = mp_inter-multiplicacao_mn_1
                mn = sub_mn_4*cb
                print("Mn =", mn,"kN.cm")
                print()
                md_inter = mn/1.1
                print ("Md =", md_inter,)
                print()
                l = comprimento*100
                l_quadrado = l*l
                conta_p = md_inter*8
                p_inter = conta_p/l_quadrado
                print("P =", p_inter,"kN/cm")
                print()

                #CALCULO DO ESFORÇO CORTANTE
                hw_to = h/tw
                div_fy = E/fy
                import math
                raiz_div = math.sqrt(div_fy)
                multiplicacao_cortante = 2.46*raiz_div
                if  hw_to <= multiplicacao_cortante:
                    print("Confere!")
                    print()
                    div_aw = largura/10
                    div2_aw = tw/10
                    aw_vd = div_aw*div2_aw
                    multiplicacao_vd = 0.6*fy*aw_vd
                    div_vd = multiplicacao_vd/1.1
                    vd = div_vd
                    print("Vd =", vd,"kN")
                    multiplicacao_p_vd = vd*2
                    div_p = multiplicacao_p_vd/l
                    print("P =", div_p,"kN")

                    #VERIFICAÇÃO DA FLECHA MÁXIMA
                    print()
                    print("Verificação da Flecha Máxima:")
                    if p_inter <= div_p:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*p_inter*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        fy_multi = fy*10
                        verificacao_fm = l/fy_multi
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg," metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                            
                        else:
                            print("Não confere!")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                    else:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*div_p*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        verificacao_fm = l/250
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg," metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere!")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                else:
                    print("Não confere!")
                    print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.") 
            else:
                print("Portanto a viga é considerada longa!")
                print()

                #CÁLCULOS
                fy_inter = fy
                mp_inter = zx*fy_inter
                print()
                print("Valor de Mp =", mp_inter,)
                subtracao_inter = fy_inter-teta_r
                mr_inter = wx*subtracao_inter
                print("Valor de Mr =", mr_inter,)
                print()
                cb = 1.14
                print("Cb =", cb,)
                sub_mn_1 = lb-lbp
                sub_mn_2 = lbr-lbp
                div_subs = sub_mn_1/sub_mn_2
                sub_mn_3 = mp_inter-mr_inter
                multiplicacao_mn_1 = sub_mn_3*div_subs
                sub_mn_4 = mp_inter-multiplicacao_mn_1
                mn = sub_mn_4*cb
                print("Mn =", mn,"kN.cm")
                print()
                md_inter = mn/1.1
                print ("Md =", md_inter,)
                print()
                l = comprimento*100
                l_quadrado = l*l
                conta_p = md_inter*8
                p_inter = conta_p/l_quadrado
                print("P =", p_inter,"kN/cm")
                print()

                #CALCULO DO ESFORÇO CORTANTE
                hw_to = h/tw
                div_fy = E/fy
                import math
                raiz_div = math.sqrt(div_fy)
                multiplicacao_cortante = 2.46*raiz_div
                if  hw_to <= multiplicacao_cortante:
                    print("Confere!")
                    print()
                    div_aw = largura/10
                    div2_aw = tw/10
                    aw_vd = div_aw*div2_aw
                    multiplicacao_vd = 0.6*fy*aw_vd
                    div_vd = multiplicacao_vd/1.1
                    vd = div_vd
                    print("Vd =", vd,"kN")
                    multiplicacao_p_vd = vd*2
                    div_p = multiplicacao_p_vd/l
                    print("P =", div_p,"kN")
                    print()

                    #VERIFICAÇÃO DA FLECHA MÁXIMA
                    print()
                    print("Verificação da Flecha Máxima:")
                    if p_inter <= div_p:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*p_inter*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        fy_multi = fy*10
                        verificacao_fm = l/fy_multi
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                    else:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*div_p*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        verificacao_fm = l/250
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere!")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                else:
                    print("Não confere!")
                    print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")                            
        else:
            print("Portanto a viga é considerada curta.")
            print()

            #CÁLCULOS
            fy_inter = fy
            mp_inter = zx*fy_inter
            print()
            print("Valor de Mp =", mp_inter,)
            subtracao_inter = fy_inter-teta_r
            mr_inter = wx*subtracao_inter
            print("Valor de Mr =", mr_inter,)
            print()
            cb = 1.14
            print("Cb =", cb,)
            print()
            fy_longa = fy
            subtracao_b1 = fy_longa-teta_r
            multiplicacao_b1 = subtracao_b1*wx
            multiplicacao_b2 = E*j
            valor_b1 = multiplicacao_b1/multiplicacao_b2
            print("B1 =", valor_b1,)
            print()
            if cw == 0:
                iy_lbr = iy
                pot_cw = h**2
                multiplicacao_cw = pot_cw*iy_lbr
                cw_longa = multiplicacao_cw/4
                print("Cw =", cw_longa,)
                print()
            else:
                cw_longa = cw
                print("Cw =", cw_longa,)
                print()
            #Fómulas
            iy_lbr = iy
            pot_lbr = valor_b1**2
            multiplicacao_lbr = 27*cw_longa*pot_lbr
            div_raiz1 = multiplicacao_lbr/iy
            mais_raiz_1 = 1+div_raiz1
            import math
            raiz_lbr_1 = math.sqrt(mais_raiz_1)
            mais_raiz_2 = 1+raiz_lbr_1
            import math
            raiz_lbr_2 = math.sqrt(mais_raiz_2)
            multiplicacao_1 = iy_lbr*j
            import math
            raiz_lbr_3 = math.sqrt(multiplicacao_1)
            multiplicacao_2 = 1.38*raiz_lbr_3
            multiplicacao_3 = j*valor_b1
            div_lbr_1 = multiplicacao_2/multiplicacao_3
            lbr = div_lbr_1*raiz_lbr_2
            pot_lbr = valor_b1**2
            multiplicacao_lbr = 27*cw*pot_lbr
            div_raiz1 = multiplicacao_lbr/iy_lbr
            mais_raiz_1 = 1+div_raiz1
            import math
            raiz_lbr_1 = math.sqrt(mais_raiz_1)
            mais_raiz_2 = 1+raiz_lbr_1
            import math
            raiz_lbr_2 = math.sqrt(mais_raiz_2)
            multiplicacao_1 = iy_lbr*j
            import math
            raiz_lbr_3 = math.sqrt(multiplicacao_1)
            multiplicacao_2 = 1.38*raiz_lbr_3
            multiplicacao_3 = j*valor_b1
            div_lbr_1 = multiplicacao_2/multiplicacao_3
            lbr = div_lbr_1*raiz_lbr_2
            print("O valor de Lbr é", lbr,"cm")
            sub_mn_1 = lb-lbp
            sub_mn_2 = lbr-lbp
            div_subs = sub_mn_1/sub_mn_2
            sub_mn_3 = mp_inter-mr_inter
            multiplicacao_mn_1 = sub_mn_3*div_subs
            sub_mn_4 = mp_inter-multiplicacao_mn_1
            mn = sub_mn_4*cb
            print("Mn =", mn,"kN.cm")
            print()
            md_inter = mn/1.1
            print ("Md =", md_inter,)
            print()
            l = comprimento*100
            l_quadrado = l*l
            conta_p = md_inter*8
            p_inter = conta_p/l_quadrado
            print("P =", p_inter,"kN/cm")
            print()

            #CALCULO DO ESFORÇO CORTANTE
            hw_to = h/tw
            div_fy = E/fy
            import math
            raiz_div = math.sqrt(div_fy)
            multiplicacao_cortante = 2.46*raiz_div
            if  hw_to <= multiplicacao_cortante:
                print("Confere!")
                div_aw = largura/10
                div2_aw = tw/10
                aw_vd = div_aw*div2_aw
                multiplicacao_vd = 0.6*fy*aw_vd
                div_vd = multiplicacao_vd/1.1
                vd = div_vd
                print("Vd =", vd,"kN")
                multiplicacao_p_vd = vd*2
                div_p = multiplicacao_p_vd/l
                print("P =", div_p,"kN")

                #VERIFICAÇÃO DA FLECHA MÁXIMA
                print()
                print("Verificação da Flecha Máxima:")
                if p_inter <= div_p:
                    I = ix
                    l_quarta = l**4
                    multiplicacao_1 = 5*p_inter*l_quarta
                    multiplicacao_2 = 384*E*I
                    flecha_maxima = multiplicacao_1/multiplicacao_2
                    print("F = ", flecha_maxima,"cm")
                    fy_multi = fy_inter*10
                    verificacao_fm = l/fy_multi
                    if flecha_maxima <= verificacao_fm:
                        print(flecha_maxima, "<", verificacao_fm,)
                        print("Confere!")
                        print()
                        print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                        print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                        print("A viga tem", comprimento,"metros de comprimento")
                        print("A viga tem", larg,"metros de largura")
                        print("A viga tem", area,"centímetros quadrados de área")
                    else:
                        print("Não confere")
                        print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada")
                else:
                    I = ix
                    l_quarta = l**4
                    multiplicacao_1 = 5*div_p*l_quarta
                    multiplicacao_2 = 384*E*I
                    flecha_maxima = multiplicacao_1/multiplicacao_2
                    print("F = ", flecha_maxima,"cm")
                    verificacao_fm = l/250
                    if flecha_maxima <= verificacao_fm:
                        print(flecha_maxima, "<", verificacao_fm,)
                        print("Confere!")
                        print()
                        print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                        print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                        print("A viga tem", comprimento,"metros de comprimento")
                        print("A viga tem", larg,"metros de largura")
                        print("A viga tem", area,"centímetros quadrados de área")
                    else:
                        print("Não confere")
                        print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada")
            else:
                print("Não confere")
                print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada")      
    else:
        secao_alma == 2
        print("Para viga de Mesa de Seção Compacta e Alma de Seção Semi Compacta")
        print("Na Mesa")
        mp = zx*fy
        print()
        print("Mp é igual a", mp,"kN.cm")
        md = mp//1.1
        print("Md é igual a", md,"kN.cm")
        print()
        print("Na Alma")
        w_semi_compacta = float(input("Digite o menor dos valores de W da seção: "))
        fy_semi_compacta = fy
        mr_alma = w_semi_compacta*fy_semi_compacta
        print("Mr = ", mr_alma,)
        print()
        mp_multi = mp
        sub_mn_1 = lamb_b_alma-alma_lamb_p
        sub_mn_2 = alma_lamb_r-alma_lamb_p
        div_lamb = sub_mn_1/sub_mn_2
        sub_mn_3 = mp_multi-mr_alma
        mn_semi_compacta = mp_multi-(div_lamb*sub_mn_3)
        print("Mn =", mn_semi_compacta)
        print()
        #Viga Curta
        teta_r = fy*0.3
        j = float(input("Digite o valor de J: "))
        print()
        print ("Verificação se a viga é considerada Curta: ")
        lb = float(input("Digite o valor de Lb (cm): "))
        E = float(input("Digite o valor de E (kN/cm2): "))
        fy_short = fy
        import math
        num = E/fy_short
        raiz = math.sqrt(num)
        lbp = 1.76*iy*raiz
        print("O valor de Lbp é", lbp,"cm")
        if  lb > lbp:
            print("Portanto a viga não é considerada curta")
            print()

            #Viga Longa
            print ("Verificação se a viga é considerada Longa: ")
            fy_longa = fy
            subtracao_b1 = fy_longa-teta_r
            multiplicacao_b1 = subtracao_b1*wx
            multiplicacao_b2 = E*j
            valor_b1 = multiplicacao_b1/multiplicacao_b2
            print("B1 =", valor_b1,)
            print()
            if cw == 0:
                iy_lbr = iy
                pot_cw = h**2
                multiplicacao_cw = pot_cw*iy_lbr
                cw_longa = multiplicacao_cw/4
                print("Cw =", cw_longa,)
                print()
            else:
                cw_longa = cw
                print("Cw =", cw_longa,)
                print()
            #Fómulas
            iy_lbr = iy
            pot_lbr = valor_b1**2
            multiplicacao_lbr = 27*cw_longa*pot_lbr
            div_raiz1 = multiplicacao_lbr/iy
            mais_raiz_1 = 1+div_raiz1
            import math
            raiz_lbr_1 = math.sqrt(mais_raiz_1)
            mais_raiz_2 = 1+raiz_lbr_1
            import math
            raiz_lbr_2 = math.sqrt(mais_raiz_2)
            multiplicacao_1 = iy_lbr*j
            import math
            raiz_lbr_3 = math.sqrt(multiplicacao_1)
            multiplicacao_2 = 1.38*raiz_lbr_3
            multiplicacao_3 = j*valor_b1
            div_lbr_1 = multiplicacao_2/multiplicacao_3
            lbr = div_lbr_1*raiz_lbr_2
            print("O valor de Lbr é", lbr,"cm")
            if  lb < lbr:
                print("Portanto a viga não é considerada longa.")
                print()

                #Viga Intermediária
                print ("Sendo assim, tem-se uma viga Intermediária: ")
                fy_inter = fy
                mp_inter = zx*fy_inter
                print()
                print("Valor de Mp =", mp_inter,)
                subtracao_inter = fy_inter-teta_r
                mr_inter = wx*subtracao_inter
                print("Valor de Mr =", mr_inter,)
                print()
                cb = 1.14
                print("Cb =", cb,)
                print()
                sub_mn_1 = lb-lbp
                sub_mn_2 = lbr-lbp
                div_subs = sub_mn_1/sub_mn_2
                sub_mn_3 = mp_inter-mr_inter
                multiplicacao_mn_1 = sub_mn_3*div_subs
                sub_mn_4 = mp_inter-multiplicacao_mn_1
                mn = sub_mn_4*cb
                print("Mn =", mn,"kN.cm")
                print()
                md_inter = mn/1.1
                print ("Md =", md_inter,)
                print()
                l = comprimento*100
                l_quadrado = l**2
                conta_p = md_inter*8
                p_inter = conta_p/l_quadrado
                print("P =", p_inter,"kN/cm")
                print()

                #CALCULO DO ESFORÇO CORTANTE
                hw_to = h/tw
                div_fy = E/fy
                import math
                raiz_div = math.sqrt(div_fy)
                multiplicacao_cortante = 2.46*raiz_div
                if  hw_to <= multiplicacao_cortante:
                    print("Confere!")
                    print()
                    div_aw = largura/10
                    div2_aw = tw/10
                    aw_vd = div_aw*div2_aw
                    multiplicacao_vd = 0.6*fy*aw_vd
                    div_vd = multiplicacao_vd/1.1
                    vd = div_vd
                    print("Vd =", vd,"kN")
                    multiplicacao_p_vd = vd*2
                    div_p = multiplicacao_p_vd/l
                    print("P =", div_p,"kN")

                    #VERIFICAÇÃO DA FLECHA MÁXIMA
                    print()
                    print("Verificação da Flecha Máxima:")
                    if p_inter <= div_p:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*p_inter*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        fy_multi = fy*10
                        verificacao_fm = l/fy_multi
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere!")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                    else:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*div_p*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        verificacao_fm = l/250
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                else:
                    print("Não confere!")
                    print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.") 
            else:
                print("Portanto a viga é considerada longa.")
                print()

                #CÁLCULOS
                fy_inter = fy
                mp_inter = zx*fy_inter
                print()
                print("Valor de Mp =", mp_inter,)
                subtracao_inter = fy_inter-teta_r
                mr_inter = wx*subtracao_inter
                print("Valor de Mr =", mr_inter,)
                print()
                cb = 1.14
                print("Cb =", cb,)
                sub_mn_1 = lb-lbp
                sub_mn_2 = lbr-lbp
                div_subs = sub_mn_1/sub_mn_2
                sub_mn_3 = mp_inter-mr_inter
                multiplicacao_mn_1 = sub_mn_3*div_subs
                sub_mn_4 = mp_inter-multiplicacao_mn_1
                mn = sub_mn_4*cb
                print("Mn =", mn,"kN.cm")
                print()
                md_inter = mn/1.1
                print ("Md =", md_inter,)
                print()
                l = comprimento*100
                l_quadrado = l*l
                conta_p = md_inter*8
                p_inter = conta_p/l_quadrado
                print("P =", p_inter,"kN/cm")
                print()

                #CALCULO DO ESFORÇO CORTANTE
                hw_to = h/tw
                div_fy = E/fy
                import math
                raiz_div = math.sqrt(div_fy)
                multiplicacao_cortante = 2.46*raiz_div
                if  hw_to <= multiplicacao_cortante:
                    print("Confere!")
                    print()
                    div_aw = largura/10
                    div2_aw = tw/10
                    aw_vd = div_aw*div2_aw
                    multiplicacao_vd = 0.6*fy*aw_vd
                    div_vd = multiplicacao_vd/1.1
                    vd = div_vd
                    print("Vd =", vd,"kN")
                    multiplicacao_p_vd = vd*2
                    div_p = multiplicacao_p_vd/l
                    print("P =", div_p,"kN")

                    #VERIFICAÇÃO DA FLECHA MÁXIMA
                    print()
                    print("Verificação da Flecha Máxima:")
                    if p_inter <= div_p:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*p_inter*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        fy_multi = fy*10
                        verificacao_fm = l/fy_multi
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere!")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                    else:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*div_p*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        verificacao_fm = l/250
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere!")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                else:
                    print("Não confere!")
                    print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")                            
        else:
            print("Portanto a viga é considerada curta.")
            print()

            #CÁLCULOS
            fy_inter = fy
            mp_inter = zx*fy_inter
            print()
            print("Valor de Mp =", mp_inter,)
            subtracao_inter = fy_inter-teta_r
            mr_inter = wx*subtracao_inter
            print("Valor de Mr =", mr_inter,)
            print()
            cb = 1.14
            print("Cb =", cb,)
            print()
            fy_longa = fy
            subtracao_b1 = fy_longa-teta_r
            multiplicacao_b1 = subtracao_b1*wx
            multiplicacao_b2 = E*j
            valor_b1 = multiplicacao_b1/multiplicacao_b2
            print("B1 =", valor_b1,)
            print()
            if cw == 0:
                iy_lbr = iy
                pot_cw = h**2
                multiplicacao_cw = pot_cw*iy_lbr
                cw_longa = multiplicacao_cw/4
                print("Cw =", cw_longa,)
                print()
            else:
                cw_longa = cw
                print("Cw =", cw_longa,)
                print()
            #Fómulas
            iy_lbr = iy
            pot_lbr = valor_b1**2
            multiplicacao_lbr = 27*cw_longa*pot_lbr
            div_raiz1 = multiplicacao_lbr/iy
            mais_raiz_1 = 1+div_raiz1
            import math
            raiz_lbr_1 = math.sqrt(mais_raiz_1)
            mais_raiz_2 = 1+raiz_lbr_1
            import math
            raiz_lbr_2 = math.sqrt(mais_raiz_2)
            multiplicacao_1 = iy_lbr*j
            import math
            raiz_lbr_3 = math.sqrt(multiplicacao_1)
            multiplicacao_2 = 1.38*raiz_lbr_3
            multiplicacao_3 = j*valor_b1
            div_lbr_1 = multiplicacao_2/multiplicacao_3
            lbr = div_lbr_1*raiz_lbr_2
            pot_lbr = valor_b1**2
            multiplicacao_lbr = 27*cw*pot_lbr
            div_raiz1 = multiplicacao_lbr/iy_lbr
            mais_raiz_1 = 1+div_raiz1
            import math
            raiz_lbr_1 = math.sqrt(mais_raiz_1)
            mais_raiz_2 = 1+raiz_lbr_1
            import math
            raiz_lbr_2 = math.sqrt(mais_raiz_2)
            multiplicacao_1 = iy_lbr*j
            import math
            raiz_lbr_3 = math.sqrt(multiplicacao_1)
            multiplicacao_2 = 1.38*raiz_lbr_3
            multiplicacao_3 = j*valor_b1
            div_lbr_1 = multiplicacao_2/multiplicacao_3
            lbr = div_lbr_1*raiz_lbr_2
            print("O valor de Lbr é", lbr,"cm")
            print()
            sub_mn_1 = lb-lbp
            sub_mn_2 = lbr-lbp
            div_subs = sub_mn_1/sub_mn_2
            sub_mn_3 = mp_inter-mr_inter
            multiplicacao_mn_1 = sub_mn_3*div_subs
            sub_mn_4 = mp_inter-multiplicacao_mn_1
            mn = sub_mn_4*cb
            print("Mn =", mn,"kN.cm")
            print()
            md_inter = mn/1.1
            print ("Md =", md_inter,)
            print()
            l = comprimento*100
            l_quadrado = l*l
            conta_p = md_inter*8
            p_inter = conta_p/l_quadrado
            print("P =", p_inter,"kN/cm")
            print()

            #CALCULO DO ESFORÇO CORTANTE
            hw_to = h/tw
            div_fy = E/fy
            import math
            raiz_div = math.sqrt(div_fy)
            multiplicacao_cortante = 2.46*raiz_div
            if  hw_to <= multiplicacao_cortante:
                print("Confere!")
                print()
                div_aw = largura/10
                div2_aw = tw/10
                aw_vd = div_aw*div2_aw
                multiplicacao_vd = 0.6*fy*aw_vd
                div_vd = multiplicacao_vd/1.1
                vd = div_vd
                print("Vd =", vd,"kN")
                multiplicacao_p_vd = vd*2
                div_p = multiplicacao_p_vd/l
                print("P =", div_p,"kN")

                #VERIFICAÇÃO DA FLECHA MÁXIMA
                print()
                print("Verificação da Flecha Máxima:")
                if p_inter <= div_p:
                    I = ix
                    l_quarta = l**4
                    multiplicacao_1 = 5*p_inter*l_quarta
                    multiplicacao_2 = 384*E*I
                    flecha_maxima = multiplicacao_1/multiplicacao_2
                    print("F = ", flecha_maxima,"cm")
                    fy_multi = fy*10
                    verificacao_fm = l/fy_multi
                    if flecha_maxima <= verificacao_fm:
                        print(flecha_maxima, "<", verificacao_fm,)
                        print("Confere!")
                        print()
                        print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                        print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                        print("A viga tem", comprimento,"metros de comprimento")
                        print("A viga tem", larg,"metros de largura")
                        print("A viga tem", area,"centímetros quadrados de área")
                    else:
                        print("Não confere!")
                        print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                else:
                    I = ix
                    l_quarta = l**4
                    multiplicacao_1 = 5*div_p*l_quarta
                    multiplicacao_2 = 384*E*I
                    flecha_maxima = multiplicacao_1/multiplicacao_2
                    print("F = ", flecha_maxima,"cm")
                    verificacao_fm = l/250
                    if flecha_maxima <= verificacao_fm:
                        print(flecha_maxima, "<", verificacao_fm,)
                        print("Confere!")
                        print()
                        print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                        print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                        print("A viga tem", comprimento,"metros de comprimento")
                        print("A viga tem", larg,"metros de largura")
                        print("A viga tem", area,"centímetros quadrados de área")
                    else:
                        print("Não confere!")
                        print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
            else:
                print("Não confere!")
                print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
#Para seção Semicompacta
elif secao_mesa == 2:
    if secao_alma ==2:
        print("Para viga de Mesa e Alma de Seção Semicompata")
        print("Na Mesa")
        fy_semi_compacta = fy
        wc_semi_compacta = float(input("Digite o valor de Wc: "))
        wr_semi_compacta = float(input("Digite o valor de Wr: "))
        z_semi_compacta = zx
        teta_r = fy_semi_compacta*0.3
        sub_semi_compacta = fy_semi_compacta-teta_r
        mr_semi_compacta = wc_semi_compacta*sub_semi_compacta
        verificacao_mr = wr_semi_compacta*fy_semi_compacta
        print("Mr na mesa =", mr_semi_compacta,)
        print()
        print("Mr=", mr_semi_compacta, "< Wr*Fy=", verificacao_mr,)
        if mr_semi_compacta <= verificacao_mr:
            print("Confere!")
            print()
            w_semi_compacta = wx
            mr_mesa = w_semi_compacta*fy_semi_compacta
            print("Mr = ", mr_mesa,)
            mp_multi = fy_semi_compacta*z_semi_compacta
            sub_mn_1 = lamb_b_mesa-mesa_lamb_p
            sub_mn_2 = mesa_lamb_r-mesa_lamb_p
            div_lamb = sub_mn_1/sub_mn_2
            sub_mn_3 = mp_multi-mr_mesa
            mn_semi_compacta = mp_multi-(div_lamb*sub_mn_3)
            print("Mn =", mn_semi_compacta,)
            print()
        else:
            print("Não confere")
            print()
        print("Na Alma")
        w_semi_compacta = float(input("Digite o valor de W da alma: "))
        mr_alma = w_semi_compacta*fy_semi_compacta
        print("Mr = ", mr_alma,)
        print()
        mp_multi = fy_semi_compacta*z_semi_compacta
        sub_mn_1 = lamb_b_alma-alma_lamb_p
        sub_mn_2 = alma_lamb_r-alma_lamb_p
        div_lamb = sub_mn_1/sub_mn_2
        sub_mn_3 = mp_multi-mr_alma
        mn_semi_compacta = mp_multi-(div_lamb*sub_mn_3)
        print("Mn =", mn_semi_compacta)
        print()

        #Viga Curta
        teta_r = fy*0.3
        j = float(input("Digite o valor de J: "))
        print()
        print ("Verificação se a viga é considerada Curta: ")
        lb = float(input("Digite o valor de Lb (cm): "))
        iy_curta = iy
        E = float(input("Digite o valor de E (kN/cm2): "))
        fy_short = fy_semi_compacta
        import math
        num = E/fy_short
        raiz = math.sqrt(num)
        lbp = 1.76*iy_curta*raiz
        print("O valor de Lbp é", lbp,"cm")
        if  lb > lbp:
            print("Portanto a viga não é considerada curta.")
            print()

            #Viga Longa
            print ("Verificação se a viga é considerada Longa: ")
            fy_longa = fy
            subtracao_b1 = fy_longa-teta_r
            multiplicacao_b1 = subtracao_b1*wx
            multiplicacao_b2 = E*j
            valor_b1 = multiplicacao_b1/multiplicacao_b2
            print("B1 =", valor_b1,)
            print()
            if cw == 0:
                iy_lbr = iy
                pot_cw = h**2
                multiplicacao_cw = pot_cw*iy_lbr
                cw_longa = multiplicacao_cw/4
                print("Cw =", cw_longa,)
                print()
            else:
                cw_longa = cw
                print("Cw =", cw_longa,)
                print()
            #Fómulas
            iy_lbr = iy
            pot_lbr = valor_b1**2
            multiplicacao_lbr = 27*cw_longa*pot_lbr
            div_raiz1 = multiplicacao_lbr/iy_lbr
            mais_raiz_1 = 1+div_raiz1
            import math
            raiz_lbr_1 = math.sqrt(mais_raiz_1)
            mais_raiz_2 = 1+raiz_lbr_1
            import math
            raiz_lbr_2 = math.sqrt(mais_raiz_2)
            multiplicacao_1 = iy_lbr*j
            import math
            raiz_lbr_3 = math.sqrt(multiplicacao_1)
            multiplicacao_2 = 1.38*raiz_lbr_3
            multiplicacao_3 = j*valor_b1
            div_lbr_1 = multiplicacao_2/multiplicacao_3
            lbr = div_lbr_1*raiz_lbr_2
            print("O valor de Lbr é", lbr,"cm")
            if  lb < lbr:
                print("Portanto a viga não é considerada longa.")
                print()

                #Viga Intermediária
                print ("Sendo assim, tem-se uma viga Intermediária: ")
                fy_inter = fy
                mp_inter = zx*fy_inter
                print()
                print("Valor de Mp =", mp_inter,)
                subtracao_inter = fy_inter-teta_r
                mr_inter = wx*subtracao_interprint("Valor de Mr =", mr_inter,)
                print()
                cb = 1.14
                print("Cb =", cb,)
                sub_mn_1 = lb-lbp
                sub_mn_2 = lbr-lbp
                div_subs = sub_mn_1/sub_mn_2
                sub_mn_3 = mp_inter-mr_inter
                multiplicacao_mn_1 = sub_mn_3*div_subs
                sub_mn_4 = mp_inter-multiplicacao_mn_1
                mn = sub_mn_4*cb
                print("Mn =", mn,"kN.cm")
                print()
                md_inter = mn/1.1
                print ("Md =", md_inter,)
                print()
                l = comprimento*100
                l_quadrado = l*l
                conta_p = md_inter*8
                p_inter = conta_p/l_quadrado
                print("P =", p_inter,"kN/cm")
                print()

                #CALCULO DO ESFORÇO CORTANTE
                fy_inter = fy
                hw_to = h/tw
                div_fy = E/fy_inter
                import math
                raiz_div = math.sqrt(div_fy)
                multiplicacao_cortante = 2.46*raiz_div
                if  hw_to <= multiplicacao_cortante:
                    print("Confere!")
                    print()
                    div_aw = largura/10
                    div2_aw = tw/10
                    aw_vd = div_aw*div2_aw
                    multiplicacao_vd = 0.6*fy_inter*aw_vd
                    div_vd = multiplicacao_vd/1.1
                    vd = div_vd
                    print("Vd =", vd,"kN")
                    multiplicacao_p_vd = vd*2
                    div_p = multiplicacao_p_vd/l
                    print("P =", div_p,"kN")
                    #VERIFICAÇÃO DA FLECHA MÁXIMA
                    print()
                    print("Verificação da Flecha Máxima:")
                    if p_inter <= div_p:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*p_inter*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        fy_multi = fy_inter*10
                        verificacao_fm = l/fy_multi
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere!")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                    else:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*div_p*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        verificacao_fm = l/250
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere!")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                else:
                    print("Não confere!")
                    print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
            else:
                print("Portanto a viga é considerada longa.")
                print()

                #CÁLCULOS
                fy_inter = fy
                mp_inter = zx*fy_inter
                print()
                print("Valor de Mp =", mp_inter,)
                subtracao_inter = fy_inter-teta_r
                mr_inter = wx*subtracao_inter
                print("Valor de Mr =", mr_inter,)
                print()
                cb = 1.14
                print("Cb =", cb,)
                sub_mn_1 = lb-lbp
                sub_mn_2 = lbr-lbp
                div_subs = sub_mn_1/sub_mn_2
                sub_mn_3 = mp_inter-mr_inter
                multiplicacao_mn_1 = sub_mn_3*div_subs
                sub_mn_4 = mp_inter-multiplicacao_mn_1
                mn = sub_mn_4*cb
                print("Mn =", mn,"kN.cm")
                print()
                md_inter = mn/1.1
                print ("Md =", md_inter,)
                print()
                l = comprimento*100
                l_quadrado = l*l
                conta_p = md_inter*8
                p_inter = conta_p/l_quadrado
                print("P =", p_inter,"kN/cm")
                print()

                #CALCULO DO ESFORÇO CORTANTE
                fy_inter = fy
                hw_to = h/tw
                div_fy = E/fy_inter
                import math
                raiz_div = math.sqrt(div_fy)
                multiplicacao_cortante = 2.46*raiz_div
                if  hw_to <= multiplicacao_cortante:
                    print("Confere!")
                    div_aw = largura/10
                    div2_aw = tw/10
                    aw_vd = div_aw*div2_aw
                    multiplicacao_vd = 0.6*fy_inter*aw_vd
                    div_vd = multiplicacao_vd/1.1
                    vd = div_vd
                    print("Vd =", vd,"kN")
                    multiplicacao_p_vd = vd*2
                    div_p = multiplicacao_p_vd/l
                    print("P =", div_p,"kN")

                    #VERIFICAÇÃO DA FLECHA MÁXIMA
                    print()
                    print("Verificação da Flecha Máxima:")
                    if p_inter <= div_p:
                        I = float(input("Digite o valor de I: "))
                        l_quarta = l**4
                        multiplicacao_1 = 5*p_inter*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        fy_multi = fy_inter*10
                        verificacao_fm = l/fy_multi
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                    else:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*div_p*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        verificacao_fm = l/250
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere!")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                else:
                    print("Não confere!")
                    print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
        else:
            print("Portanto a viga é considerada curta.")
            print()

            #CÁLCULOS
            fy_inter = fy
            mp_inter = zx*fy_inter
            print()
            print("Valor de Mp =", mp_inter,)
            subtracao_inter = fy_inter-teta_r
            mr_inter = wx*subtracao_inter
            print("Valor de Mr =", mr_inter,)
            print()
            cb = 1.14
            print("Cb =", cb,)
            print()
            fy_longa = fy
            subtracao_b1 = fy_longa-teta_r
            multiplicacao_b1 = subtracao_b1*wx
            multiplicacao_b2 = E*j
            valor_b1 = multiplicacao_b1/multiplicacao_b2
            print("B1 =", valor_b1,)
            print()
            if cw == 0:
                iy_lbr = iy
                pot_cw = h**2
                multiplicacao_cw = pot_cw*iy_lbr
                cw_longa = multiplicacao_cw/4
                print("Cw =", cw_longa,)
                print()
            else:
                cw_longa = cw
                print("Cw =", cw_longa,)
                print()
            #Fómulas
            iy_lbr = iy
            pot_lbr = valor_b1**2
            multiplicacao_lbr = 27*cw_longa*pot_lbr
            div_raiz1 = multiplicacao_lbr/iy_lbr
            mais_raiz_1 = 1+div_raiz1
            import math
            raiz_lbr_1 = math.sqrt(mais_raiz_1)
            mais_raiz_2 = 1+raiz_lbr_1
            import math
            raiz_lbr_2 = math.sqrt(mais_raiz_2)
            multiplicacao_1 = iy_lbr*j
            import math
            raiz_lbr_3 = math.sqrt(multiplicacao_1)
            multiplicacao_2 = 1.38*raiz_lbr_3
            multiplicacao_3 = j*valor_b1
            div_lbr_1 = multiplicacao_2/multiplicacao_3
            lbr = div_lbr_1*raiz_lbr_2
            pot_lbr = valor_b1**2
            multiplicacao_lbr = 27*cw*pot_lbr
            div_raiz1 = multiplicacao_lbr/iy_lbr
            mais_raiz_1 = 1+div_raiz1
            import math
            raiz_lbr_1 = math.sqrt(mais_raiz_1)
            mais_raiz_2 = 1+raiz_lbr_1
            import math
            raiz_lbr_2 = math.sqrt(mais_raiz_2)
            multiplicacao_1 = iy_lbr*j
            import math
            raiz_lbr_3 = math.sqrt(multiplicacao_1)
            multiplicacao_2 = 1.38*raiz_lbr_3
            multiplicacao_3 = j*valor_b1
            div_lbr_1 = multiplicacao_2/multiplicacao_3
            lbr = div_lbr_1*raiz_lbr_2
            print("O valor de Lbr é", lbr,"cm")
            sub_mn_1 = lb-lbp
            sub_mn_2 = lbr-lbp
            div_subs = sub_mn_1/sub_mn_2
            sub_mn_3 = mp_inter-mr_inter
            multiplicacao_mn_1 = sub_mn_3*div_subs
            sub_mn_4 = mp_inter-multiplicacao_mn_1
            mn = sub_mn_4*cb
            print("Mn =", mn,"kN.cm")
            print()
            md_inter = mn/1.1
            print ("Md =", md_inter,)
            print()
            l = comprimento*100
            l_quadrado = l*l
            conta_p = md_inter*8
            p_inter = conta_p/l_quadrado
            print("P =", p_inter,"kN/cm")
            print()

            #CALCULO DO ESFORÇO CORTANTE
            hw_to = h/tw
            div_fy = E/fy_inter
            import math
            raiz_div = math.sqrt(div_fy)
            multiplicacao_cortante = 2.46*raiz_div
            if  hw_to <= multiplicacao_cortante:
                print("Confere!")
                div_aw = largura/10
                div2_aw = tw/10
                aw_vd = div_aw*div2_aw
                multiplicacao_vd = 0.6*fy_inter*aw_vd
                div_vd = multiplicacao_vd/1.1
                vd = div_vd
                print("Vd =", vd,"kN")
                multiplicacao_p_vd = vd*2
                div_p = multiplicacao_p_vd/l
                print("P =", div_p,"kN")

                #VERIFICAÇÃO DA FLECHA MÁXIMA
                print()
                print("Verificação da Flecha Máxima:")
                if p_inter <= div_p:
                    I = ix
                    l_quarta = l**4
                    multiplicacao_1 = 5*p_inter*l_quarta
                    multiplicacao_2 = 384*E*I
                    flecha_maxima = multiplicacao_1/multiplicacao_2
                    print("F = ", flecha_maxima,"cm")
                    fy_multi = fy_inter*10
                    verificacao_fm = l/fy_multi
                    if flecha_maxima <= verificacao_fm:
                        print(flecha_maxima, "<", verificacao_fm,)
                        print("Confere!")
                        print()
                        print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                        print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                        print("A viga tem", comprimento,"metros de comprimento")
                        print("A viga tem", larg,"metros de largura")
                        print("A viga tem", area,"centímetros quadrados de área")
                    else:
                        print("Não confere!")
                        print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                else:
                    I = ix
                    l_quarta = l**4
                    multiplicacao_1 = 5*div_p*l_quarta
                    multiplicacao_2 = 384*E*I
                    flecha_maxima = multiplicacao_1/multiplicacao_2
                    print("F = ", flecha_maxima,"cm")
                    verificacao_fm = l/250
                    if flecha_maxima <= verificacao_fm:
                        print(flecha_maxima, "<", verificacao_fm,)
                        print("Confere!")
                        print()
                        print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                        print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                        print("A viga tem", comprimento,"metros de comprimento")
                        print("A viga tem", larg,"metros de largura")
                        print("A viga tem", area,"centímetros quadrados de área")
                    else:
                        print("Não confere!")
                        print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
            else:
                print("Não confere!")
                print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
    else:
        secao_alma == 1
        print("Para viga de Mesa de Seção Semicompata e Alma de Seção Compacta")
        print("Na Mesa")
        fy_semi_compacta = fy
        wc_semi_compacta = float(input("Digite o valor de Wc: "))
        wr_semi_compacta = float(input("Digite o valor de Wr: "))
        z_semi_compacta = zx
        teta_r = fy_semi_compacta*0.3
        sub_semi_compacta = fy_semi_compacta-teta_r
        mr_semi_compacta = wc_semi_compacta*sub_semi_compacta
        verificacao_mr = wr_semi_compacta*fy_semi_compacta
        print("Mr na mesa =", mr_semi_compacta,)
        print()
        print("Mr=", mr_semi_compacta, "< Wr*Fy=", verificacao_mr,)
        if mr_semi_compacta <= verificacao_mr:
            print("Confere!")
            print()
            w_semi_compacta = wx
            mr_mesa = w_semi_compacta*fy_semi_compacta
            print("Mr = ", mr_mesa,)
            mp_multi = fy_semi_compacta*z_semi_compacta
            sub_mn_1 = lamb_b_mesa-mesa_lamb_p
            sub_mn_2 = mesa_lamb_r-mesa_lamb_p
            div_lamb = sub_mn_1/sub_mn_2
            sub_mn_3 = mp_multi-mr_mesa
            mn_semi_compacta = mp_multi-(div_lamb*sub_mn_3)
            print("Mn =", mn_semi_compacta,)
            print()
            print("Na alma")
            mp = zx*fy
            print()
            print("Mp é igual a", mp,"kN.cm")
            md = mp//1.1
            print("Md é igual a", md,"kN.cm")
            print()
            #Viga Curta
            teta_r = fy*0.3
            j = float(input("Digite o valor de J: "))
            print()
            print ("Verificação se a viga é considerada Curta: ")
            lb = float(input("Digite o valor de Lb (cm): "))
            iy_curta = iy
            E = float(input("Digite o valor de E (kN/cm2): "))
            fy_short = fy
            import math
            num = E/fy_short
            raiz = math.sqrt(num)
            lbp = 1.76*iy_curta*raiz
            print("O valor de Lbp é", lbp,"cm")
            if  lb > lbp:
                print("Portanto a viga não é considerada curta.")
                print()

                #Viga Longa
                print ("Verificação se a viga é considerada Longa: ")
                fy_longa = fy
                subtracao_b1 = fy_longa-teta_r
                multiplicacao_b1 = subtracao_b1*wx
                multiplicacao_b2 = E*j
                valor_b1 = multiplicacao_b1/multiplicacao_b2
                print("B1 =", valor_b1,)
                print()
                if cw == 0:
                    iy_lbr = iy
                    pot_cw = h**2
                    multiplicacao_cw = pot_cw*iy_lbr
                    cw_longa = multiplicacao_cw/4
                    print("Cw =", cw_longa,)
                    print()
                else:
                    cw_longa = cw
                    print("Cw =", cw_longa,)
                    print()
                    
                #Fómulas
                iy_lbr = iy
                pot_lbr = valor_b1**2
                multiplicacao_lbr = 27*cw_longa*pot_lbr
                div_raiz1 = multiplicacao_lbr/iy_lbr
                mais_raiz_1 = 1+div_raiz
                import math
                raiz_lbr_1 = math.sqrt(mais_raiz_1)
                mais_raiz_2 = 1+raiz_lbr_1
                import math
                raiz_lbr_2 = math.sqrt(mais_raiz_2)
                multiplicacao_1 = iy_lbr*j
                import math
                raiz_lbr_3 = math.sqrt(multiplicacao_1)
                multiplicacao_2 = 1.38*raiz_lbr_3
                multiplicacao_3 = j*valor_b1
                div_lbr_1 = multiplicacao_2/multiplicacao_3
                lbr = div_lbr_1*raiz_lbr_2
                print("O valor de Lbr é", lbr,"cm")
                if  lb < lbr:
                    print("Portanto a viga não é considerada longa.")
                    print()
                    #Viga Intermediária
                    print ("Sendo assim, tem-se uma viga Intermediária: ")
                    fy_inter = fy
                    mp_inter = zx*fy_inter
                    print()
                    print("Valor de Mp =", mp_inter,)
                    subtracao_inter = fy_inter-teta_r
                    mr_inter = wx*subtracao_inter
                    print("Valor de Mr =", mr_inter,)
                    print()
                    cb = 1.14
                    print("Cb =", cb,)
                    sub_mn_1 = lb-lbp
                    sub_mn_2 = lbr-lbp
                    div_subs = sub_mn_1/sub_mn_2
                    sub_mn_3 = mp_inter-mr_inter
                    multiplicacao_mn_1 = sub_mn_3*div_subs
                    sub_mn_4 = mp_inter-multiplicacao_mn_1
                    mn = sub_mn_4*cb
                    print("Mn =", mn,"kN.cm")
                    print()
                    md_inter = mn/1.1
                    print ("Md =", md_inter,)
                    print()
                    l = comprimento*100
                    l_quadrado = l*l
                    conta_p = md_inter*8
                    p_inter = conta_p/l_quadrado
                    print("P =", p_inter,"kN/cm")
                    print()

                    #CALCULO DO ESFORÇO CORTANTE
                    hw_to = h/tw
                    div_fy = E/fy_inter
                    import math
                    raiz_div = math.sqrt(div_fy)
                    multiplicacao_cortante = 2.46*raiz_div
                    if  hw_to <= multiplicacao_cortante:
                        print("Confere!")
                        print()
                        div_aw = largura/10
                        div2_aw = tw/10
                        aw_vd = div_aw*div2_aw
                        multiplicacao_vd = 0.6*fy_inter*aw_vd
                        div_vd = multiplicacao_vd/1.1
                        vd = div_vd
                        print("Vd =", vd,"kN")
                        multiplicacao_p_vd = vd*2
                        div_p = multiplicacao_p_vd/l
                        print("P =", div_p,"kN")

                        #VERIFICAÇÃO DA FLECHA MÁXIMA
                        print()
                        print("Verificação da Flecha Máxima:")
                        if p_inter <= div_p:
                            I = ix
                            l_quarta = l**4
                            multiplicacao_1 = 5*p_inter*l_quarta
                            multiplicacao_2 = 384*E*I
                            flecha_maxima = multiplicacao_1/multiplicacao_2
                            print("F= ", flecha_maxima,"cm")
                            fy_multi = fy_inter*10
                            verificacao_fm = l/fy_multi
                            if flecha_maxima <= verificacao_fm:
                                print(flecha_maxima, "<", verificacao_fm,)
                                print("Confere!")
                                print()
                                print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                                print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                                print("A viga tem", comprimento,"metros de comprimento")
                                print("A viga tem", larg,"metros de largura")
                                print("A viga tem", area,"centímetros quadrados de área")
                            else:
                                print("Não confere!")
                                print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                        else:
                            I = ix
                            l_quarta = l**4
                            multiplicacao_1 = 5*div_p*l_quarta
                            multiplicacao_2 = 384*E*I
                            flecha_maxima = multiplicacao_1/multiplicacao_2
                            print("F = ", flecha_maxima,"cm")
                            verificacao_fm = l/250
                            if flecha_maxima <= verificacao_fm:
                                print(flecha_maxima, "<", verificacao_fm,)
                                print("Confere!")
                                print()
                                print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                                print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                                print("A viga tem", comprimento,"metros de comprimento")
                                print("A viga tem", larg,"metros de largura")
                                print("A viga tem", area,"centímetros quadrados de área")
                            else:
                                print("Não confere!")
                                print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                    else:
                        print("Não confere!")
                        print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                else:
                    print("Portanto a viga é considerada longa.")
                    print()
                    #CÁLCULOS
                    fy_inter = fy
                    mp_inter = zx*fy_inter
                    print()
                    print("Valor de Mp =", mp_inter,)
                    subtracao_inter = fy_inter-teta_r
                    mr_inter = wx*subtracao_inter
                    print("Valor de Mr =", mr_inter,)
                    print()
                    cb = 1.14
                    fy_longa = fy
                    subtracao_b1 = fy_longa-teta_r
                    multiplicacao_b1 = subtracao_b1*wx
                    multiplicacao_b2 = E*j
                    valor_b1 = multiplicacao_b1/multiplicacao_b2
                    print("B1 =", valor_b1,)
                    print()
                    if cw == 0:
                        iy_lbr = iy
                        pot_cw = h**2
                        multiplicacao_cw = pot_cw*iy_lbr
                        cw_longa = multiplicacao_cw/4
                        print("Cw =", cw_longa,)
                        print()
                    else:
                        cw_longa = cw
                        print("Cw =", cw_longa,)
                        print()
                
                    #Fómulas
                    iy_lbr = iy
                    pot_lbr = valor_b1**2
                    multiplicacao_lbr = 27*cw_longa*pot_lbr
                    div_raiz1 = multiplicacao_lbr/iy_lbr
                    print("Cb =", cb,)
                    sub_mn_1 = lb-lbp
                    sub_mn_2 = lbr-lbp
                    div_subs = sub_mn_1/sub_mn_2
                    sub_mn_3 = mp_inter-mr_inter
                    multiplicacao_mn_1 = sub_mn_3*div_subs
                    sub_mn_4 = mp_inter-multiplicacao_mn_1
                    mn = sub_mn_4*cb
                    print("Mn =", mn,"kN.cm")
                    print()
                    md_inter = mn/1.1
                    print ("Md =", md_inter,)
                    print()
                    l = comprimento*100
                    l_quadrado = l*l
                    conta_p = md_inter*8
                    p_inter = conta_p/l_quadrado
                    print("P =", p_inter,"kN/cm")
                    print()

                    #CALCULO DO ESFORÇO CORTANTE
                    hw_to = h/tw
                    div_fy = E/fy_inter
                    import math
                    raiz_div = math.sqrt(div_fy)
                    multiplicacao_cortante = 2.46*raiz_div
                    if  hw_to <= multiplicacao_cortante:
                        print("Confere!")
                        print()
                        div_aw = largura/10
                        div2_aw = tw/10
                        aw_vd = div_aw*div2_aw
                        multiplicacao_vd = 0.6*fy_inter*aw_vd
                        div_vd = multiplicacao_vd/1.1
                        vd = div_vd
                        print("Vd =", vd,"kN")
                        multiplicacao_p_vd = vd*2
                        div_p = multiplicacao_p_vd/l
                        print("P =", div_p,"kN")

                        #VERIFICAÇÃO DA FLECHA MÁXIMA
                        print()
                        print("Verificação da Flecha Máxima:")
                        if p_inter <= div_p:
                            I = ix
                            l_quarta = l**4
                            multiplicacao_1 = 5*p_inter*l_quarta
                            multiplicacao_2 = 384*E*I
                            flecha_maxima = multiplicacao_1/multiplicacao_2
                            print("F = ", flecha_maxima,"cm")
                            fy_multi = fy_inter*10
                            verificacao_fm = l/fy_multi
                            if flecha_maxima <= verificacao_fm:
                                print(flecha_maxima, "<", verificacao_fm,)
                                print("Confere!")
                                print()
                                print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                                print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                                print("A viga tem", comprimento,"metros de comprimento")
                                print("A viga tem", larg,"metros de largura")
                                print("A viga tem", area,"centímetros quadrados de área")
                            else:
                                print("Não confere!")
                                print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                        else:
                            I = ix
                            l_quarta = l**4
                            multiplicacao_1 = 5*div_p*l_quarta
                            multiplicacao_2 = 384*E*I
                            flecha_maxima = multiplicacao_1/multiplicacao_2
                            print("F = ", flecha_maxima,"cm")
                            verificacao_fm = l/250
                            if flecha_maxima <= verificacao_fm:
                                print(flecha_maxima, "<", verificacao_fm,)
                                print("Confere!")
                                print()
                                print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                                print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                                print("A viga tem", comprimento,"metros de comprimento")
                                print("A viga tem", larg,"metros de largura")
                                print("A viga tem", area,"centímetros quadrados de área")
                            else:
                                print("Não confere!")
                                print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                    else:
                        print("Não confere!")
                        print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
            else:
                print("Portanto a viga é considerada curta.")
                print()

                #CÁLCULOS
                fy_inter = fy
                mp_inter = zx*fy_inter
                print()
                print("Valor de Mp =", mp_inter,)
                subtracao_inter = fy_inter-teta_r
                mr_inter = wx*subtracao_inter
                print("Valor de Mr =", mr_inter,)
                print()
                cb = 1.14
                print("Cb =", cb,)
                print()
                fy_longa = fy
                subtracao_b1 = fy_longa-teta_r
                multiplicacao_b1 = subtracao_b1*wx
                multiplicacao_b2 = E*j
                valor_b1 = multiplicacao_b1/multiplicacao_b2
                print("B1 =", valor_b1,)
                print()
                if cw == 0:
                    iy_lbr = iy
                    pot_cw = h**2
                    multiplicacao_cw = pot_cw*iy_lbr
                    cw_longa = multiplicacao_cw/4
                    print("Cw =", cw_longa,)
                    print()
                else:
                    cw_longa = cw
                    print("Cw =", cw_longa,)
                    print()
                
                #Fómulas
                iy_lbr = iy
                pot_lbr = valor_b1**2
                multiplicacao_lbr = 27*cw_longa*pot_lbr
                div_raiz1 = multiplicacao_lbr/iy_lbr
                mais_raiz_1 = 1+div_raiz1
                import math
                raiz_lbr_1 = math.sqrt(mais_raiz_1)
                mais_raiz_2 = 1+raiz_lbr_1
                import math
                raiz_lbr_2 = math.sqrt(mais_raiz_2)
                multiplicacao_1 = iy_lbr*j
                import math
                raiz_lbr_3 = math.sqrt(multiplicacao_1)
                multiplicacao_2 = 1.38*raiz_lbr_3
                multiplicacao_3 = j*valor_b1
                div_lbr_1 = multiplicacao_2/multiplicacao_3
                lbr = div_lbr_1*raiz_lbr_2
                print("O valor de Lbr é", lbr,"cm")
                sub_mn_1 = lb-lbp
                sub_mn_2 = lbr-lbp
                div_subs = sub_mn_1/sub_mn_2
                sub_mn_3 = mp_inter-mr_inter
                multiplicacao_mn_1 = sub_mn_3*div_subs
                sub_mn_4 = mp_inter-multiplicacao_mn_1
                mn = sub_mn_4*cb
                print("Mn =", mn,"kN.cm")
                print()
                md_inter = mn/1.1
                print ("Md =", md_inter,)
                print()
                l = comprimento*100
                l_quadrado = l*l
                conta_p = md_inter*8
                p_inter = conta_p/l_quadrado
                print("P =", p_inter,"kN/cm")
                print()

                #CALCULO DO ESFORÇO CORTANTE
                hw_to = h/tw
                div_fy = E/fy_inter
                import math
                raiz_div = math.sqrt(div_fy)
                multiplicacao_cortante = 2.46*raiz_div
                if  hw_to <= multiplicacao_cortante:
                    print("Confere!")
                    print()
                    div_aw = largura/10
                    div2_aw = tw/10
                    aw_vd = div_aw*div2_aw
                    multiplicacao_vd = 0.6*fy_inter*aw_vd
                    div_vd = multiplicacao_vd/1.1
                    vd = div_vd
                    print("Vd =", vd,"kN")
                    multiplicacao_p_vd = vd*2
                    div_p = multiplicacao_p_vd/l
                    print("P =", div_p,"kN")

                    #VERIFICAÇÃO DA FLECHA MÁXIMA
                    print()
                    print("Verificação da Flecha Máxima:")
                    if p_inter <= div_p:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*p_inter*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F = ", flecha_maxima,"cm")
                        fy_multi = fy_inter*10
                        verificacao_fm = l/fy_multi
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere!")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                    else:
                        I = ix
                        l_quarta = l**4
                        multiplicacao_1 = 5*div_p*l_quarta
                        multiplicacao_2 = 384*E*I
                        flecha_maxima = multiplicacao_1/multiplicacao_2
                        print("F= ", flecha_maxima,"cm")
                        verificacao_fm = l/250
                        if flecha_maxima <= verificacao_fm:
                            print(flecha_maxima, "<", verificacao_fm,)
                            print("Confere!")
                            print()
                            print("Portanto o peso resistente da viga será ", p_inter,"kN/cm.")
                            print("A carga total aplicada será de: ",pesop+wall+laje+carga_acidental,"kN/m")
                            print("A viga tem", comprimento,"metros de comprimento")
                            print("A viga tem", larg,"metros de largura")
                            print("A viga tem", area,"centímetros quadrados de área")
                        else:
                            print("Não confere!")
                            print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
                else:
                    print("Não confere!")
                    print("Deve-se realizar alterações pois a viga não está suportando a carga distribuída informada.")
    


#Implementar tamanho de viga: OK!
    #Colocar carregamento acidental: OK!
    #Viga Curta: OK!
    #Viga Intermediária: OK!
    #Viga Longa: OK!
    #Combinação:
    #Semi compacta: (1/2 OK!)
    #Verificação do momento teórico
    #Classificação de curto intermediário e longo:
    #CB= 1,14: (OK!)
    #Qual o carregamento distribido que pode dar em cima da viga
    
    
    
