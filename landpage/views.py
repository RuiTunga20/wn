from django.shortcuts import render,redirect
from django.template import RequestContext
from landpage.models import *
import os
import zipfile
from django.http import HttpResponse
from django.conf import settings
from pathlib import Path
from landpage.form import InscricaoForm,EmpresaForm,encontrosb2bForm,EmpresaFormPatrocinio,Inscricao_empresaForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import ImageDraw,ImageFont
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from django.contrib.auth.models import User
from django.template.context_processors import request
from django.contrib import messages




def enviar_email(Email,imagem,nome):
    
    

    try:



        # Carrega a imagem como uma string binária
        
        # Cria um objeto EmailMultiAlternatives


        # Define o remetente, destinatário e assunto do e-mail
        Nome=nome

        me = 'workshop@mirempet.ao'
        you = Email
        msg = MIMEMultipart()
        msg['Subject'] = 'Convite para workshop de rochas ornamentais'
        msg['From'] = me
        msg['To'] = you

        # Abre o arquivo de imagem e adiciona ao e-mail
        with open(str(os.path.join(settings.MEDIA_ROOT,str(imagem) )), 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', '<image1>')
            msg.attach(img)

        # Adiciona o corpo do e-mail
        html = f"""\
        <!DOCTYPE html>
            <html lang="pt-br">
            <head>
            <meta charset="UTF-8">
            <title>Convite para workshop de rochas ornamentais</title>
            </head>
            <body>
            <p>Olá {Nome},</p>
            <p>Espero que esteja tudo bem com você.</p>
            <p>O seu pedido de inscrição para o Workshop e Exposição de Rochas Ornamentais a ser realizado na Huíla nos dias 26 e 27 de Outubro foi aceite.</p>
           
            <p><a href="https://eventos.mirempet.ao"> Mais informações sobre o programa click aqui.</a></p>

            
           
            <img src="cid:image1" height="700" width="500">
            <br><br>
           
            </body>
            </html>        """
        part2 = MIMEText(html, 'html')
        msg.attach(part2)

        # Envia o e-mail
        s = smtplib.SMTP_SSL('mail.mirempet.ao', 465)
        s.login('workshop@mirempet.ao', '@WORKSHOP2023@')
        s.sendmail(me, you, msg.as_string())
        s.quit()
        smserro="Foi lhe enviado um email com o banner"
        return redirect('/')


    except Exception as e:
        smserro=str(e)+" erro"
        print(smserro)


def enviar_Empresa(Email,imagem,nome,id):

    try:



        # Carrega a imagem como uma string binária
        
        # Cria um objeto EmailMultiAlternatives


        # Define o remetente, destinatário e assunto do e-mail
        Nome=nome

        me = 'workshop@mirempet.ao'
        you = Email
        msg = MIMEMultipart()
        msg['Subject'] = 'Convite para workshop de rochas ornamentais'
        msg['From'] = me
        msg['To'] = you

        # Abre o arquivo de imagem e adiciona ao e-mail
        with open(str(os.path.join(settings.MEDIA_ROOT,str(imagem) )), 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', '<image1>')
            msg.attach(img)

        # Adiciona o corpo do e-mail
        html = f"""\
        <!DOCTYPE html>
            <html lang="pt-br">
            <head>
            <meta charset="UTF-8">
            <title>Convite para workshop de rochas ornamentais</title>
            </head>
            <body>
            <p>Olá {Nome},</p>
            <p>Espero que esteja tudo bem com você.</p>
            <p>O seu pedido de inscrição para o Workshop e Exposição de Rochas Ornamentais a ser realizado na Huíla nos dias 26 e 27 de Outubro foi aceite.</p>
           
            <p> Mais informações sobre o programa click <a href="https://eventos.mirempet.ao">aqui.</a></p>
            <p>
            Para cadastrar os participantes, click em <a href="https://eventos.mirempet.ao/Empresa-Participante/{id}">Resgistrar Participantes</a></p>
:
            </p>

           


            
           
            <img src="cid:image1" height="700" width="500">
            <br><br>
           
            </body>
            </html>        """
        part2 = MIMEText(html, 'html')
        msg.attach(part2)

        # Envia o e-mail
        s = smtplib.SMTP_SSL('mail.mirempet.ao', 465)
        s.login('workshop@mirempet.ao', '@WORKSHOP2023@')
        s.sendmail(me, you, msg.as_string())
        s.quit()
        smserro="Foi lhe enviado um email com o banner"
        return redirect('/')


    except Exception as e:
        smserro=str(e)+" erro"
        print(smserro)

def enviar_email_post(Email,nome):
    try:



        # Carrega a imagem como uma string binária
        
        # Cria um objeto EmailMultiAlternatives


        # Define o remetente, destinatário e assunto do e-mail
        Nome=nome

        me = 'workshop@mirempet.ao'
        you = Email
        msg = MIMEMultipart()
        msg['Subject'] = 'Inscrição para workshop de rochas ornamentais'
        msg['From'] = me
        msg['To'] = you

        # Abre o arquivo de imagem e adiciona ao e-mail
       

        # Adiciona o corpo do e-mail
        html = f"""\
        <!DOCTYPE html>
            <html lang="pt-br">
            <head>
            <meta charset="UTF-8">
            <title>Convite para workshop de rochas ornamentais</title>
            </head>
            <body>
            <p>Olá {Nome},</p>
            <p>O seu pedido de inscrição para o Workshop e Exposição de Rochas Ornamentais a ser realizado na Huíla nos dias 26 e 27 de Outubro está a ser processado. Deverá receberá informações adicionais.</p>
            <p>Deverá enviar o comprovativo do pagamento neste email</p>
            <h4>Informações Bancárias</h4>
            <p><strong>Banco:</strong> BFA</p>
            <p><strong>IBAN N°:</strong> 0006.0000.1606.7872.3014.9</p>
            <p>
            Contactos Para Participação:

            Rua Rainha Ginga 127 b 1º Andar, Luanda-Angola
            Tel: +244 943 892 207 | 939 515 161
            </p>

            <p>O Workshop abordará os seguintes tópicos:</p>
           
            <p><a href="https://eventos.mirempet.ao"> Mais informações sobre o programa click aqui.</a></p>

            
            
           
            </body>
            </html>        """
        part2 = MIMEText(html, 'html')
        msg.attach(part2)

        # Envia o e-mail
        s = smtplib.SMTP_SSL('mail.mirempet.ao', 465)
        s.login('workshop@mirempet.ao', '@WORKSHOP2023@')
        s.sendmail(me, you, msg.as_string())
        s.quit()
        smserro="Foi lhe enviado um email com o banner"
        return redirect('/')


    except Exception as e:
        smserro=str(e)+" erro"
        print(smserro)


def enviar_email_individual_visita(Email,nome,enail_user,empresa,pacote):
    try:



        # Carrega a imagem como uma string binária
        
        # Cria um objeto EmailMultiAlternatives


        # Define o remetente, destinatário e assunto do e-mail
        Nome=nome
        id=Inscricao.objects.get(email=enail_user)

        me = 'workshop@mirempet.ao'
        you = Email
        msg = MIMEMultipart()
        msg['Subject'] = 'Novo registro para o ROA 2023'
        msg['From'] = me
        msg['To'] = you

        # Abre o arquivo de imagem e adiciona ao e-mail
       

        # Adiciona o corpo do e-mail
        html = f"""\
        <!DOCTYPE html>
            <html lang="pt-br">
            <head>
            <meta charset="UTF-8">
            <title></title>
            </head>
            <body>
                <p>
                  Recebeu uma nova solicitação de registro para o workshop com os seguintes detalhes::
                  <ul>
                    <li>Nome: <b>{Nome}</b></li>
                    <li>Endereço de e-mail: <b>{enail_user}</b></li>
                    <li>Empresa: <b>{empresa}</b></li>
                    <li>Pacote: <b>{pacote}</b></li>


                  </ul>
                </p>
                <p>
                  Para validar a solicitaão, acesse o sistema através do link abaixo:
                 <a href="https://eventos.mirempet.ao/Painel-Controlelandpage/inscricao/?q={id.id}" target="_blank"> <br> Validar solicitação</a></p>

                </p>
                
                <p>Agradecemos a sua atenção.</p>
                <p>Atenciosamente,</p>
           

            
            
           
            </body>
            </html>        """
        part2 = MIMEText(html, 'html')
        msg.attach(part2)

        # Envia o e-mail
        s = smtplib.SMTP_SSL('mail.mirempet.ao', 465)
        s.login('workshop@mirempet.ao', '@WORKSHOP2023@')
        s.sendmail(me, you, msg.as_string())
        s.quit()
        smserro="Foi lhe enviado um email com o banner"
        return redirect('/')


    except Exception as e:
        smserro=str(e)+" erro"
        print(smserro)
   
def enviar_email_Empresa(Email,nome,enail_user,pacote):
    try:



        # Carrega a imagem como uma string binária
        
        # Cria um objeto EmailMultiAlternatives


        # Define o remetente, destinatário e assunto do e-mail
        
        id=Empresa.objects.get(email=enail_user)
        me = 'workshop@mirempet.ao'
        you = Email
        msg = MIMEMultipart()
        msg['Subject'] = 'Novo registro para o ROA 2023'
        msg['From'] = me
        msg['To'] = you
        pacote=Pacotes_Patrocinio.objects.get(id=pacote)

        # Abre o arquivo de imagem e adiciona ao e-mail
       

        # Adiciona o corpo do e-mail
        html = f"""\
        <!DOCTYPE html>
            <html lang="pt-br">
            <head>
            <meta charset="UTF-8">
            <title></title>
            </head>
            <body>
                <p>
                  Recebeu uma nova solicitação de registro para o workshop com os seguintes detalhes::
                  <ul>
                    <li>Empresa: <b>{nome}</b></li>
                    <li>Endereço de e-mail: <b>{enail_user}</b></li>
                    <li>Pacote: <b>{pacote}</b></li>


                  </ul>
                </p>
                <p>
                  Para validar a solicitaão, acesse o sistema através do link abaixo:
                 <a href="https:/eventos.mirempet.ao/Painel-Controlelandpage/empresa/?q={id.id}" target="_blank"> <br> Validar solicitação</a></p>

                </p>
                
                <p>Agradecemos a sua atenção.</p>
                <p>Atenciosamente,</p>
           

            
            
           
            </body>
            </html>        """
        part2 = MIMEText(html, 'html')
        msg.attach(part2)

        # Envia o e-mail
        s = smtplib.SMTP_SSL('mail.mirempet.ao', 465)
        s.login('workshop@mirempet.ao', '@WORKSHOP2023@')
        s.sendmail(me, you, msg.as_string())
        s.quit()
        smserro="Foi lhe enviado um email com o banner"
        return redirect('/')


    except Exception as e:
        smserro=str(e)+" erro"
        print(smserro)
   






def download_folder(request,id):
    # Caminho da pasta que contém os arquivos que deseja baixar
    BASE_DIR = Path(__file__).resolve().parent.parent


    folder_path = os.path.join(settings.MEDIA_ROOT, id)

    #print(id)



    # Nome do arquivo zip que será criado
    zip_filename = id+'.zip'

    # Cria um arquivo zip
    zip_file = zipfile.ZipFile(zip_filename, 'w')

    # Adiciona todos os arquivos da pasta ao arquivo zip
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            print(file)
            file_path = os.path.join(root, file)
            zip_file.write(file_path, os.path.relpath(file_path, folder_path))

    # Fecha o arquivo zip
    zip_file.close()

    # Cria uma resposta de download para o arquivo zip
    response = HttpResponse(open(zip_filename, 'rb').read())
    response['Content-Type'] = 'application/zip'
    response['Content-Disposition'] = 'attachment; filename="%s"' % zip_filename

    # Retorna a resposta de download
    return response


def home(request):
    Prelectores= prelector.objects.all()
    Moderador= moderador.objects.all()
    Dia_1=Programa1.objects.all()
    Dia_2=Programa2.objects.all()
    Noticias=NOTICIA.objects.all()

    context={
        'Prelectores':Prelectores,
        'Moderador':Moderador,
        'Dia_1':Dia_1,
        'Dia_2':Dia_2,
        'Noticias':Noticias,

    }


    return redirect ('/Eventos/1')


def Eventos(request):
    

    return redirect ('/Eventos/1')

def Eventos_detalhes(request,id):
    form=InscricaoForm(request.POST)

    if request.POST:
        if form.is_valid():
            inscricao = form.save()
            return redirect('/789')
    else:
        form=InscricaoForm(request.POST)


        
    complex={
      'form':form  
    }
    

    return render(request,'index_detalhes.html',complex)


def formulario(request):
    form=InscricaoForm(request.POST)

    if request.POST:
        if form.is_valid():
            try:
                 inscricao = form.save()

            except Exception as e:
                print(e)

            enviar_email_post(request.POST.get("email"),request.POST.get("nome"))
            enviar_email_individual_visita('roa.workshop@mirempet.ao',request.POST.get("nome"),request.POST.get("email"),request.POST.get("empresa"),request.POST.get("Convidados"))
            return redirect('/')
    else:
        form=InscricaoForm(request.POST)


        
    complex={
      'form':form  
    }
    

    return render(request,'formulario.html',complex)

def formularioEntreEmpresa(request):
    form=encontrosb2bForm(request.POST)

    if request.POST:
        if form.is_valid():
            try:
                 form.save()

            except Exception as e:
                print(e)

            enviar_email_post(request.POST.get("email"),request.POST.get("nome"))
            enviar_email_Empresa('roa.workshop@mirempet.ao',request.POST.get("nome"),request.POST.get("email"),request.POST.get("Pacotes"))

            return redirect('/')
    else:
        form=encontrosb2bForm(request.POST)


        
    complex={
      'form':form  
    }
    

    return render(request,'empresa.html',complex)


def formularioEmpresa(request):
    form=EmpresaForm(request.POST)

    if request.POST:
        if form.is_valid():
            try:
                 form.save()

            except Exception as e:
                print(e)

            enviar_email_post(request.POST.get("email"),request.POST.get("nome"))
            enviar_email_Empresa('roa.workshop@mirempet.ao',request.POST.get("nome"),request.POST.get("email"),request.POST.get("Pacotes"))

            return redirect('/')
    else:
        form=EmpresaForm(request.POST)


        
    complex={
      'form':form  
    }
    

    return render(request,'entreempresa.html',complex)

def formularioEmpresaPatrocinio(request):
    form=EmpresaFormPatrocinio(request.POST)

    if request.POST:
        if form.is_valid():
            try:
                 form.save()

            except Exception as e:
                print(e)

            enviar_email_post(request.POST.get("email"),request.POST.get("nome"))
            enviar_email_Empresa('roa.workshop@mirempet.ao',request.POST.get("nome"),request.POST.get("email"),request.POST.get("Pacotes"))

            return redirect('/')
    else:
        form=EmpresaFormPatrocinio(request.POST)


        
    complex={
      'form':form  
    }
    

    return render(request,'empresapatrocinio.html',complex)
def formulario_empresa(request,id):
    sms=""
    form=Inscricao_empresaForm(request.POST)
    empresa=Empresa.objects.get(id=id)
    if  len (Inscricao_empresa.objects.filter(empresa=id)) <  empresa.Pacotes.participantes:
        if request.POST:
            if form.is_valid():
                try:
                    novo=form.save(commit=False)
                    novo.empresa=empresa
                    novo.save()
                    messages.add_message(request, messages.SUCCESS, "Cadastrado com Sucesso!.")
                    enviar_email_post(request.POST.get("email"),request.POST.get("nome"))
                    enviar_email_Empresa('roa.workshop@mirempet.ao',request.POST.get("nome"),request.POST.get("email"),request.POST.get("Pacotes"))

                    return redirect('/Empresa-Participante/'+str(id))





                except Exception as e:
                    print(e)
            else:
                messages.add_message(request, messages.WARNING, str(form.errors))



                #enviar_email_post(request.POST.get("email"),request.POST.get("nome"))
                ##enviar_email_Empresa('roa.workshop@mirempet.ao',request.POST.get("nome"),request.POST.get("email"),request.POST.get("Pacotes"))

                return redirect('/Empresa-Participante/'+str(id))
        else:
                form=Inscricao_empresaForm(request.POST)
    else:
        messages.add_message(request, messages.INFO, "Atigiu o limite maximo de inscrição!")

        


        
    complex={
      'form':form,
      'empresa':Empresa.objects.get(id=id)
    }

    return render (request,'registro_empresa.html',complex)

def godigoqr(nome):
        data = 'https://eventos.mirempet.ao/convidado/' + str(nome)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(os.path.join(settings.MEDIA_ROOT, f'qrcode_{nome}.png'))

def convidadeo(request,id):
    try:
         convidado=Inscricao.objects.get(id=id)
         print(convidado.pacote)

    except:
        convidado="teste"

    context={
        'convidado':convidado
    }
    return render(request,'convidado.html',context)

def pacoteparticipacao(request):
    return render(request,'pacotePa.html')

def patrocinio(request):
    return render(request,'pacotePro.html')

    # Faz algo com o usuário
    
@receiver(post_save, sender=Inscricao)
def enviar_email_ao_aceitar(sender, instance, **kwargs):

        
        
        if instance.estado == 'Aceite' and  instance.image == "Vazio" :
            

            fnt = ImageFont.truetype(os.path.join(settings.MEDIA_ROOT, "Montserrat-ExtraBold.otf"), 150)

            # Enviar email com imagem

            godigoqr(instance.id)  # Gera o código QR

            # Abre o código QR gerado
            qr_image = Image.open(os.path.join(settings.MEDIA_ROOT, f'qrcode_{instance.id}.png'))

            # Abre a imagem associada a esta instância
            pil_img = Image.open(os.path.join(settings.MEDIA_ROOT, 'RUI.png'))
            draw = ImageDraw.Draw(pil_img)
            draw.text((290, 810), instance.Convidados, (255, 182, 0),fnt)

            # Redimensiona o código QR
            nova_largura = 300
            nova_altura = 300
            imagem_redimensionada = qr_image.resize((nova_largura, nova_altura))

            # Sobreponha o código QR redimensionado à imagem
            pil_img.paste(imagem_redimensionada, (530, 1250), imagem_redimensionada)

            # Salva a imagem final processada com um nome específico na pasta de mídia
            nome_imagem_final = f'Tomas_qrcode_{instance.id}.png'
            caminho_imagem_final = os.path.join(settings.MEDIA_ROOT, nome_imagem_final)
            pil_img.save(caminho_imagem_final)
           
            
            os.remove(os.path.join(settings.MEDIA_ROOT, f'qrcode_{instance.id}.png'))
            edita=Inscricao.objects.get(id=instance.id)
            edita.image=nome_imagem_final
            #edita.user_updadte=User.objects.get(id=request.user.id)

            edita.save()
            try:
                imagem=Inscricao.objects.get(id=instance.id)
                enviar_email(instance.email,imagem.image,imagem.nome)
            except Exception as e:
                print(e)

@receiver(post_save, sender=Empresa)
def enviar_email_ao_aceitar(sender, instance, **kwargs):



        if instance.estado == 'Aceite' and  instance.image == "Vazio" or instance.image == "" :
            

            fnt = ImageFont.truetype(os.path.join(settings.MEDIA_ROOT, "Montserrat-ExtraBold.otf"), 109)

            # Enviar email com imagem

            godigoqr(instance.id)  # Gera o código QR

            # Abre o código QR gerado
            qr_image = Image.open(os.path.join(settings.MEDIA_ROOT, f'qrcode_{instance.id}.png'))

            # Abre a imagem associada a esta instância
            print(instance.Pacotes.nome)
            if 'Negro' in instance.Pacotes.nome:
                pil_img = Image.open(os.path.join(settings.MEDIA_ROOT, 'RUI.png'))
                draw = ImageDraw.Draw(pil_img)
                draw.text((290, 840), instance.Pacotes.nome, (255, 182, 0),fnt)
            else:
                pil_img = Image.open(os.path.join(settings.MEDIA_ROOT, 'RUI.png'))
                draw = ImageDraw.Draw(pil_img)
                draw.text((170, 840), instance.Pacotes.nome, (255, 182, 0),fnt)

            # Redimensiona o código QR
            nova_largura = 300
            nova_altura = 300
            imagem_redimensionada = qr_image.resize((nova_largura, nova_altura))

            # Sobreponha o código QR redimensionado à imagem
            pil_img.paste(imagem_redimensionada, (530, 1250), imagem_redimensionada)

            # Salva a imagem final processada com um nome específico na pasta de mídia
            nome_imagem_final = f'Tomas_qrcode_{instance.id}.png'
            caminho_imagem_final = os.path.join(settings.MEDIA_ROOT, nome_imagem_final)
            pil_img.save(caminho_imagem_final)


            os.remove(os.path.join(settings.MEDIA_ROOT, f'qrcode_{instance.id}.png'))
            edita=Empresa.objects.get(id=instance.id)
            edita.image=nome_imagem_final
            #edita.user_updadte=User.objects.get(id=request.user.id)

            edita.save()
            try:
                imagem=Empresa.objects.get(id=instance.id)
                enviar_Empresa(instance.email,imagem.image,imagem.nome,instance.id)

            except Exception as e:
                print(e)
       
@receiver(post_save, sender=EmpresaPatrocinio)
def enviar_email_ao_aceitar(sender, instance, **kwargs):

        

        if instance.estado == 'Aceite' and  instance.image == "Vazio" or instance.image == "" :
            

            fnt = ImageFont.truetype(os.path.join(settings.MEDIA_ROOT, "Montserrat-ExtraBold.otf"), 109)

            # Enviar email com imagem

            godigoqr(instance.id)  # Gera o código QR

            # Abre o código QR gerado
            qr_image = Image.open(os.path.join(settings.MEDIA_ROOT, f'qrcode_{instance.id}.png'))

            # Abre a imagem associada a esta instância
            print(instance.Pacotes.nome)
            if 'Branco' not in instance.Pacotes.nome:
                pil_img = Image.open(os.path.join(settings.MEDIA_ROOT, 'RUI.png'))
                draw = ImageDraw.Draw(pil_img)
                draw.text((290, 840), instance.Pacotes.nome, (255, 182, 0),fnt)
            else:
                pil_img = Image.open(os.path.join(settings.MEDIA_ROOT, 'RUI.png'))
                draw = ImageDraw.Draw(pil_img)
                draw.text((170, 840), instance.Pacotes.nome, (255, 182, 0),fnt)

            # Redimensiona o código QR
            nova_largura = 300
            nova_altura = 300
            imagem_redimensionada = qr_image.resize((nova_largura, nova_altura))

            # Sobreponha o código QR redimensionado à imagem
            pil_img.paste(imagem_redimensionada, (530, 1250), imagem_redimensionada)

            # Salva a imagem final processada com um nome específico na pasta de mídia
            nome_imagem_final = f'Tomas_qrcode_{instance.id}.png'
            caminho_imagem_final = os.path.join(settings.MEDIA_ROOT, nome_imagem_final)
            pil_img.save(caminho_imagem_final)


            os.remove(os.path.join(settings.MEDIA_ROOT, f'qrcode_{instance.id}.png'))
            edita=EmpresaPatrocinio.objects.get(id=instance.id)
            edita.image=nome_imagem_final
            #edita.user_updadte=User.objects.get(id=request.user.id)

            edita.save()
            try:
                imagem=EmpresaPatrocinio.objects.get(id=instance.id)
                enviar_email(instance.email,imagem.image,imagem.nome)
            except Exception as e:
                print(e)

@receiver(post_save, sender=Inscricao_empresa)
def enviar_Empresa_registro(sender, instance, **kwargs,):
        if instance.image == "Vazio" :
            

            fnt = ImageFont.truetype(os.path.join(settings.MEDIA_ROOT, "Montserrat-ExtraBold.otf"), 109)

            # Enviar email com imagem

            godigoqr(instance.id)  # Gera o código QR

            # Abre o código QR gerado
            qr_image = Image.open(os.path.join(settings.MEDIA_ROOT, f'qrcode_{instance.id}.png'))

            # Abre a imagem associada a esta instância
            if 'Negro' in instance.empresa.Pacotes.nome:
                pil_img = Image.open(os.path.join(settings.MEDIA_ROOT, 'RUI.png'))
                draw = ImageDraw.Draw(pil_img)
                draw.text((290, 840), instance.empresa.Pacotes.nome, (255, 182, 0),fnt)
            else:
                pil_img = Image.open(os.path.join(settings.MEDIA_ROOT, 'RUI.png'))
                draw = ImageDraw.Draw(pil_img)
                draw.text((170, 840), instance.empresa.Pacotes.nome, (255, 182, 0),fnt)

            # Redimensiona o código QR
            nova_largura = 300
            nova_altura = 300
            imagem_redimensionada = qr_image.resize((nova_largura, nova_altura))

            # Sobreponha o código QR redimensionado à imagem
            pil_img.paste(imagem_redimensionada, (530, 1250), imagem_redimensionada)

            # Salva a imagem final processada com um nome específico na pasta de mídia
            nome_imagem_final = f'Tomas_qrcode_{instance.id}.png'
            caminho_imagem_final = os.path.join(settings.MEDIA_ROOT, nome_imagem_final)
            pil_img.save(caminho_imagem_final)
           
            
            os.remove(os.path.join(settings.MEDIA_ROOT, f'qrcode_{instance.id}.png'))
            edita=Inscricao_empresa.objects.get(id=instance.id)
            edita.image=nome_imagem_final
            #edita.user_updadte=User.objects.get(id=request.user.id)

            edita.save()
            try:
                imagem=Inscricao_empresa.objects.get(id=instance.id)
                enviar_email(instance.email,imagem.image,imagem.nome)
            except Exception as e:
                print(e)



@receiver(post_save, sender=encontrosb2b)
def enviar_Empresa_registro(sender, instance, **kwargs,):
        if instance.estado == 'Aceite' and  instance.image == "Vazio" or instance.image == "" :
            

            fnt = ImageFont.truetype(os.path.join(settings.MEDIA_ROOT, "Montserrat-ExtraBold.otf"), 109)

            # Enviar email com imagem

            godigoqr(instance.id)  # Gera o código QR

            # Abre o código QR gerado
            qr_image = Image.open(os.path.join(settings.MEDIA_ROOT, f'qrcode_{instance.id}.png'))

            # Abre a imagem associada a esta instância
            pil_img = Image.open(os.path.join(settings.MEDIA_ROOT, 'RUI.png'))
            draw = ImageDraw.Draw(pil_img)
            draw.text((290, 840), 'Delegado B2B', (255, 182, 0),fnt)
        

            # Redimensiona o código QR
            nova_largura = 300
            nova_altura = 300
            imagem_redimensionada = qr_image.resize((nova_largura, nova_altura))

            # Sobreponha o código QR redimensionado à imagem
            pil_img.paste(imagem_redimensionada, (530, 1250), imagem_redimensionada)

            # Salva a imagem final processada com um nome específico na pasta de mídia
            nome_imagem_final = f'Tomas_qrcode_{instance.id}.png'
            caminho_imagem_final = os.path.join(settings.MEDIA_ROOT, nome_imagem_final)
            pil_img.save(caminho_imagem_final)
           
            
            os.remove(os.path.join(settings.MEDIA_ROOT, f'qrcode_{instance.id}.png'))
            edita=encontrosb2b.objects.get(id=instance.id)
            edita.image=nome_imagem_final
            #edita.user_updadte=User.objects.get(id=request.user.id)

            edita.save()
            try:
                imagem=encontrosb2b.objects.get(id=instance.id)
                enviar_email(instance.email,imagem.image,imagem.nome)
            except Exception as e:
                print(e)