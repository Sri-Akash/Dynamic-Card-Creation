const imageUrl = document.getElementById('imageUrl')
const name = document.getElementById('name')
const category = document.getElementById('category')
const stock = document.getElementById('stock')
const price = document.getElementById('price')
const description = document.getElementById('description')
const productId = document.getElementById("productId")

const form = document.querySelector('form')
const loadProductContainer = document.querySelector("#loadProductContainer")

form.addEventListener('submit', function (event) {
    event.preventDefault()

    const formData = new FormData(form)
    const data = Object.fromEntries(formData)

    if (productId.value) {
        updateData(data, productId.value)
    }else{
        postData(data)
    }
    getData()
})

document.addEventListener("DOMContentLoaded", () => {
    getData()
})


function postData(data) {
    fetch("/product/new", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            if (data.status == "success") {
                alert(data.message)
            }
            else {
                throw new Error(data.message);
            }
        })
        .catch(err => {
            alert(err)
        })
}

function getData() {
    fetch("/product/getAll")
        .then(response => response.json())
        .then(data => {
            if (data.status == "success") {
                loadProductContainer.innerHTML = ""

                let productList = data.data

                productList.forEach(product => {
                    let cardSnippet = `
                        <div class="card">
                            <div class="card-header" style="background-image: url(${product.imageUrl})">
                                <div class="d-flex justify-content-between align-items-center">
                                    <i class="bi bi-pencil-fill edit-btn" data-id="${product.id}"></i>
                                    <i class="bi bi-trash3-fill delete-btn" data-id="${product.id}"></i>
                                </div>
                            </div>
                            <div class="card-body">
                                <div class="name-n-price d-flex justify-content-between align-items-baseline">
                                    <h3 class="fs-5">${product.name}</h3>
                                    <p class="price fs-5">₹${product.price}</p>
                                </div>
                                <p class="description">${product.description}</p>
                                <div class="category-n-stock d-flex justify-content-between align-items-center flex-wrap gap-2">
                                    <div class="badge badge-primary text-break">
                                        ${product.category}
                                    </div>
                                    <div class="badge badge-secondary">
                                        ${product.stock} Left
                                    </div>
                                </div>
                            </div>
                        </div>
                    `
                    loadProductContainer.innerHTML += cardSnippet
                });
            }
            else {
                throw new Error(data.message);
            }
        })
        .catch(err => {
            alert(err)
        })
}

loadProductContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("edit-btn")) {
        let id = e.target.dataset.id
        console.log(id)
        fetchSingleProduct(id)
    }

    if (e.target.classList.contains("delete-btn")) {
        let id = e.target.dataset.id
        console.log(id)

        if (confirm("Do you want to delete?")){
            deleteProduct(id)
        }
    }
})


function fetchSingleProduct(id) {
    fetch(`/product/getSingle?id=${id}`)
        .then(response => response.json())
        .then(dataResponse => {
            if (dataResponse.status == "success") {
                const data = dataResponse.data

                imageUrl.value = data.imageUrl
                name.value = data.name
                category.value = data.category
                stock.value = data.stock
                price.value = data.price
                description.value = data.description

                productId.value = data.id
            }
            else {
                throw new Error(dataResponse.message);
            }
        })
        .catch(err => {
            alert(err)
        })
}


function updateData(data, id) {
    fetch(`/product/update?id=${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            if (data.status == "success") {
                alert(data.message)
                getData()
            }
            else {
                throw new Error(data.message);
            }
        })
        .catch(err => {
            alert(err)
        })
}

function deleteProduct(id) {
    fetch(`/product/delete?id=${id}`, {
        method: "DELETE",
    })
        .then(response => response.json())
        .then(data => {
            if (data.status == "success") {
                alert(data.message)
                getData()
            }
            else {
                throw new Error(data.message);
            }
        })
        .catch(err => {
            alert(err)
        })
}

function deleteProducts(id) {
    fetch(`/product/delete?id=${id}`, {
        method: "DELETE",
    })
        .then(response => response.json())
        .then(data => {
            if (data.status == "success") {
                alert(data.message)
                getData()
            }
            else {
                throw new Error(data.message);
            }
        })
        .catch(err => {
            alert(err)
        })
}