let zona = document.querySelector('.zona-noticias')

async function data() {
    let data = await fetch('http://192.168.1.103:8000/getNotices/').then(res=>res.json());
    zona.innerHTML = ''
    let noticias = data.noticias
    if ( noticias ) {
        for (const noticia of noticias) {
            // console.log(noticia.title)
            zona.innerHTML += `
            <div class="card text-start">
                <img class="card-img-top" src="http://192.168.1.103/DJANGO/test-noticias/img/notice.jpg" style="width:100%; height:240px; object-fit: cover;" alt="Card image cap">
                <div class="card-body">
                    <h4 class="card-title">Titulo: ${noticia.title}</h4>
                    <p class="card-text">Text: ${noticia.text}</p>
                    <a href="#" class="card-link">Card link</a>
                    <a href="#" class="card-link">Another link</a>
                </div>
            </div>
            <br>
            `
        }

        zona.innerHTML += `
        <div class="btn btn-primary" role="alert" onclick="data()">
        <strong>¿No hay más?</strong> Pulsa para recargar <i class="fa-solid fa-rotate-right fa-spin" style="color: #fff;"></i>
        </div>
        `

    } else {
        zona.innerHTML = `
            <div class="card mb-3 my-4 m-auto" style="max-width: 540px;">
                <div class="row g-0">
                    <div class="col-md-4">
                        <img src="http://192.168.1.103/DJANGO/test-noticias/img/no-notice.jpg" class="img-fluid rounded-start" alt="Card title">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                        <h5 class="card-title">No se han Encontrado Noticias</h5>
                        <p class="card-text">Hemos recorrido todo el ciberespacio, pero no hemos encontrado nada.</p>
                        <button class="btn btn-outline-primary" onclick="data()">Actualizar</button>
                        </div>
                    </div>
                </div>
            </div>
        `
    }
}
data()