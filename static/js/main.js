// Variables
var addToCartBtn = document.getElementsByClassName('add-to-cart')
var num = document.querySelector(".num")
var	hamburger = document.getElementById('hamburger')
var menu = document.getElementById('menu')
var body = document.querySelector('.container')


// Menu toggle
hamburger.addEventListener('click', function (){
    if (menu.style.display == "flex"){
        menu.style.display = "none"
    }else{
        menu.style.display = "flex"
    }
})

// Add to cart function
for (var i = 0; i < addToCartBtn.length; i++) {
	addToCartBtn[i].addEventListener('click', function(){
		var productId = this.dataset.product
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
		.then(refreshCart, (data) => {alert(data)})
		.then(green)
		.then(setTimeout(grey,1500))
	})
}


// Refresh cart items function
function refreshCart(){
	fetch(refreshUrl, {
		method: 'POST',
		credentials: 'same-origin',
		headers: {
			"X-CSRFToken": csrfToken,
			'Content-Type':'application/json',
		},
		body: JSON.stringify({
			'deviceId': deviceId,
		})
	})
	.then((res) => {
		return res.json()
	})
	.then((data) => {
		num.innerHTML = data
	})
}

// Green flash to notify the custumer that an item has been added to cart
function green() {
	body.style.background = "green"
}
function grey() {
	body.style.background = "#f4f4f4"
}