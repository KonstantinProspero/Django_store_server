from django.shortcuts import render

# Create your views here.
# контроллеры

def index(request):
	context = {
		'title': 'Store',
	    'is_promotion': False ,
	}
	return render(request, 'products/index.html', context)

def products(request):
	context = {
		'title': 'Store - Каталог',
		'products': [
			{
				'image': "/static/vendor/img/products/Adidas-hoodie.png",
				'name': "Худи черного цвета с монограммами adidas Originals",
				'price': "6090",
				'description': "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни."
			},
			{
				'image': "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
				'name': "Синяя куртка The North Face",
				'price': "2372",
				'description': "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель."
			},
			{
				'image': "/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
				'name': "Коричневый спортивный oversized-топ ASOS DESIGN",
				'price': "6090",
				'description': "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни."
			},
			{
				'image': "/static/vendor/img/products/Adidas-hoodie.png",
				'name': "Худи черного цвета с монограммами adidas Originals",
				'price': "3390",
				'description': "Материал с плюшевой текстурой. Удобный и мягкий."
			},
			{
				'image': "/static/vendor/img/products/Black-Nike-Heritage-backpack.png",
				'name': "Черный рюкзак Nike Heritage",
				'price': "2340",
				'description': "Плотная ткань. Легкий материал."
			},
			{
				'image': "/static/vendor/img/products/Black-Dr-Martens-shoes.png",
				'name': "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
				'price': "1359",
				'description': "Гладкий кожаный верх. Натуральный материал."
			}
		]
	 
	}
	return render(request, 'products/products.html', context)