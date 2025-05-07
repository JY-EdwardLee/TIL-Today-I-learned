/* 
  아래에 코드를 작성해주세요.
*/

const searchBtn = document.querySelector('.search-box__button')
const API_URL = 'http://ws.audioscrobbler.com/2.0/'
const API_KEY = 'f55d6ecc5e3240a7e6e84f6d37a923e8'
const inputTag = document.querySelector('.search-box__input');
const searchResult = document.querySelector('.search-result')
const fetchAlbums = function(page=1, limit=10){
const keyword = inputTag.value;
  axios({
    method : 'get',
    url : API_URL,
    params : {
      limit : limit,
      page : page,
      method: 'album.search',
      album : keyword,
      api_key : API_KEY,
      format : 'json'
      }
  })
  .then ((response => {
    console.log(response)
    for (const i in response.data.results.albummatches.album){
    const album = response.data.results.albummatches.album[i]
    const {artist, name} = album
    const url = album.url
      // 이미지 태그 만들기
    const cardImg = document.createElement('img')
    const artistTag = document.createElement('h3')
    const nameTag = document.createElement('p')
    cardImg.src = album.image[0]['#text']
    
    // div 태그 만들고 클래스 부여햐기
    const card = document.createElement('div')
    const text = document.createElement('div')
    text.classList.add('search-result__text')
    card.classList.add('search-result__card')

    // 앨버명, 가수명 입력하기
    artistTag.textContent = artist
    nameTag.textContent = name
    // div 태그에 이미지 태그 추가하기
    card.append(cardImg)
    text.append(artistTag)
    text.append(nameTag)
    card.appendChild(text)
    searchResult.appendChild(card)
    card.addEventListener('click', () => {
      window.open(url, '_blank')
    })
  }}))
  .catch((response => {
    console.log(response)
  }))
}
searchBtn.addEventListener('click', fetchAlbums)