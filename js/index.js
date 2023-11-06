
function setup_paintings_block(){
    panintings_block = document.getElementById("paintings")

    const paintings = db.paintings

    paintings.forEach(element => {
        panintings_block.innerHTML += `
        <div class="painting">

            <a class="painting_picture" href="./painting.html?slug=${element.slug}">
                <img src="images/${element.filename}" alt="${element.slug}">
            </a>

            <a class="painting_info" href="./painting.html?slug=${element.slug}">
                <h2>${element.title}</h2>
                <p>${element.short_description}</p>
            </a>
            
        </div>
            `
    });
}

setup_paintings_block()