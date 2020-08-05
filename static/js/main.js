var addToCartBtn = document.getElementsByClassName('add-to-cart')

for (var i = 0; i < addToCartBtn.length; i++) {
	addToCartBtn[i].addEventListener('click', function(){
		var productId = this.dataset.product
		console.log(productId)
		fetch(addToCartUrl, {
			method: 'POST',
			credentials: 'same-origin',
			headers: {
				"X-CSRFToken": csrfToken,
				'Content-Type':'application/json',
			},
			body: JSON.stringify({
				'productId': productId,
				'user': user,
				'deviceId': deviceId,
			})
		})
		.then((res) => {
			return res.json()
		})
		.then((data) => {
			alert(data)
		})
	})
}

var	hamburger = document.getElementById('hamburger')
var menu = document.getElementById('menu')
hamburger.addEventListener('click', function (){
    if (menu.style.display == "flex"){
        menu.style.display = "none"
    }else{
        menu.style.display = "flex"
    }
})