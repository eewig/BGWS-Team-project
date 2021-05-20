async function likePost(post_id){
	const imgsUrls = new Array('/static/posts/like_active.png','/static/posts/like.png');
	const likeDiv = document.getElementById("likes-" + post_id);
	const image = likeDiv.getElementsByTagName('img')[0];
	const likesTag = likeDiv.getElementsByClassName('likes-number')[0];
	const baseUrl = location.origin + "/like/" + post_id + "?" + "like="
	const likesNumber = Number.parseInt(likesTag.textContent, 10)

	if(image.src.indexOf('like.png') > 0){
		const response = await fetch(baseUrl + "true");
		if (response.url.indexOf("/users/login/")>0){
			window.location.replace(response.url);
		}
		else{
			const jsonResponse = await response.json();
			if (jsonResponse['ok'] == "true"){
				image.src=imgsUrls[0];
				likesTag.textContent = likesNumber + 1;
			}
		}
	}else {
		fetch(baseUrl + "false")
		.then(function(response) {
			return response.json();
		})
		.then(function(jsonResponse) {
			if (jsonResponse['ok'] == "true"){
				image.src=imgsUrls[1];
				likesTag.textContent = likesNumber - 1;
			}
		});
			
	}
}
