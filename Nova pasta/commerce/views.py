from django.shortcuts import render, get_object_or_404,redirect
from .models import Produtos
from .forms import ProdutosForm


def administracao(request):
    total_produtos = Produtos.objects.count()
    
    context = {
        'total_produtos' : total_produtos,
    }
    return render(request,"commerce/admins.html",context)

def produtos_cadastrar(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProdutosForm()
    else:
        form = ProdutosForm()

    return render(request, "commerce/form.html", {'form': form})


def produto_editar(request,id):
    produto = get_object_or_404(Produtos,id=id)
   
    if request.method == 'POST':
        form = ProdutosForm(request.POST,instance=produto)

        if form.is_valid():
            form.save()
            return redirect('produtos_listar')
    else:
        form = ProdutosForm(instance=produto)

    return render(request,'commerce/form.html',{'form':form})


def produto_remover(request, id):
    produto = get_object_or_404(Produtos, id=id)
    produto.delete()
    return redirect('produtos_listar') # procure um url com o nome 'lista_aluno'

def index(request):
    produtos = Produtos.objects.all()
    context ={
        'produtos':produtos
    }
    return render(request, "commerce/index.html",context)

def produtos_listar(request):
    produtos = Produtos.objects.all()
    return render(request, "commerce/produtos.html",{'produtos':produtos})

def detalhe_produto(request, id):
    produtos = get_object_or_404(Produtos, id=id)
    context={'produtos' : produtos}
    
    return render(request,'commerce/detalhe.html', context)

