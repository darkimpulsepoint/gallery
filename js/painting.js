function setup_painting(){

    params = new URLSearchParams(window.location.search)
    const slug=params.get("slug")

    painting = get_painting_by_slug(slug)
    
    document.title=painting.title

    innerHTML = `
    <div class="painting_picture">
                <img src="./images/${painting.filename}" alt="${painting.title}">
            </div>
            <div class="painting_info">
                <h3>
                    ${painting.title}
                </h3>
                <p>`
    innerHTML += `<div class="description">`

    painting.full_description.forEach(el => {
        innerHTML += `<p>${el}</p>`
   })
   
    innerHTML += `</div></div>`
    
    const painting_block = document.getElementById("painting")
    painting_block.innerHTML = innerHTML


    const currentPaintingPos = get_posiion_by_slug(slug)
    const paintingsAmount = get_paintings_amount()

    const prevPainting = get_painting_by_pos((currentPaintingPos-1+paintingsAmount)%paintingsAmount)
    const nextPainting = get_painting_by_pos((currentPaintingPos+1+paintingsAmount)%paintingsAmount)

    const navigation = document.getElementById("navigation")
    navigation.innerHTML = `
        <div class="prev">
            <a href="painting.html?slug=${prevPainting.slug}"><-${prevPainting.title}</a>
        </div>
        <div class="next">
            <a href="painting.html?slug=${nextPainting.slug}">${nextPainting.title}-></a>
        </div>
    `
}

setup_painting()