<script context="module" lang="ts">
	export async function load({ fetch }) {
		if (browser && get(isUserAuthenticated)) {
			try {
				const res = await fetch(captureEndpoint, {
					method: "GET",
					headers: new Headers({
						Accept: "application/json",
						"Content-Type": "application/json",
						Authorization: `Bearer ${get(userToken).access}`
					})
				});
				const data = await res.json();
				return {
					props: {
						backendVimeVolume: data.video_volume
					}
				};
			} catch (err) {
				if (err instanceof Error) {
					userToken.set({ refresh: "", access: "" });
					console.error(`Can't fetch from backend | Flushing Tokens | Reason : ${err.message}`);
				}
			}
		}
		return {
			props: {
				backendVimeVolume: 0
			}
		};
	}
</script>

<script lang="ts">
	export let backendVimeVolume: number;
	$: {
		if (backendVimeVolume !== 0 && backendVimeVolume) {
			browser && localStorage.setItem("vimejs-volume", JSON.stringify(~~backendVimeVolume));
		}
	}
	let textContent = `
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget nunc lobortis mattis aliquam faucibus purus in massa tempor. In ornare quam viverra orci sagittis. Et netus et malesuada fames ac. Lobortis scelerisque fermentum dui faucibus in ornare quam viverra orci. Imperdiet nulla malesuada pellentesque elit. Tortor posuere ac ut consequat semper viverra nam. Nunc sed id semper risus in. Tellus in hac habitasse platea dictumst vestibulum rhoncus. Id diam maecenas ultricies mi. Id nibh tortor id aliquet lectus proin nibh nisl. Fames ac turpis egestas sed tempus urna et. Porttitor lacus luctus accumsan tortor posuere ac. Varius quam quisque id diam. Sapien pellentesque habitant morbi tristique senectus et netus et. Et tortor at risus viverra adipiscing at. Nibh nisl condimentum id venenatis a condimentum. Pharetra massa massa ultricies mi quis hendrerit dolor magna eget.

Nulla pellentesque dignissim enim sit amet venenatis urna cursus eget. A diam sollicitudin tempor id eu nisl nunc mi. Amet massa vitae tortor condimentum lacinia quis. Mattis rhoncus urna neque viverra justo nec. At tellus at urna condimentum mattis. Vitae semper quis lectus nulla at volutpat diam ut venenatis. Neque ornare aenean euismod elementum nisi quis eleifend. Augue eget arcu dictum varius duis at consectetur lorem. Sed adipiscing diam donec adipiscing. In nulla posuere sollicitudin aliquam ultrices sagittis orci a. Aliquam malesuada bibendum arcu vitae. Pharetra et ultrices neque ornare aenean. Ridiculus mus mauris vitae ultricies leo integer malesuada nunc. Pharetra diam sit amet nisl. Senectus et netus et malesuada fames. Sit amet luctus venenatis lectus magna fringilla urna porttitor. Sit amet nisl suscipit adipiscing bibendum est ultricies integer quis. Nibh sit amet commodo nulla facilisi. Imperdiet sed euismod nisi porta lorem.

Dui sapien eget mi proin sed libero. Neque viverra justo nec ultrices dui sapien eget mi proin. Lectus arcu bibendum at varius vel. In cursus turpis massa tincidunt dui ut ornare. Turpis egestas maecenas pharetra convallis. Fringilla phasellus faucibus scelerisque eleifend. Diam donec adipiscing tristique risus nec feugiat. Sit amet mattis vulputate enim nulla aliquet porttitor. Dolor sed viverra ipsum nunc aliquet bibendum enim facilisis. Accumsan tortor posuere ac ut consequat semper viverra nam. Aliquam ut porttitor leo a diam sollicitudin tempor id eu. Donec adipiscing tristique risus nec feugiat in fermentum posuere urna. Mauris a diam maecenas sed. Hac habitasse platea dictumst quisque sagittis purus sit. Suspendisse potenti nullam ac tortor vitae purus faucibus ornare. Mi ipsum faucibus vitae aliquet. Elementum curabitur vitae nunc sed velit dignissim. Ullamcorper sit amet risus nullam eget felis eget. Nibh tortor id aliquet lectus proin.

A iaculis at erat pellentesque adipiscing. Dolor sed viverra ipsum nunc aliquet. Nullam non nisi est sit amet. Egestas dui id ornare arcu odio ut sem nulla. Egestas maecenas pharetra convallis posuere morbi leo urna molestie at. Rhoncus mattis rhoncus urna neque viverra justo nec ultrices. Faucibus purus in massa tempor nec. Vitae sapien pellentesque habitant morbi tristique. Facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat. Proin libero nunc consequat interdum varius sit. Aenean euismod elementum nisi quis eleifend quam adipiscing vitae. Adipiscing elit ut aliquam purus sit. Tortor vitae purus faucibus ornare suspendisse sed nisi lacus. Mus mauris vitae ultricies leo integer malesuada nunc vel. Eget nulla facilisi etiam dignissim diam quis enim lobortis scelerisque.

At auctor urna nunc id cursus. Tellus in metus vulputate eu scelerisque felis. Augue lacus viverra vitae congue eu consequat ac felis. Id diam maecenas ultricies mi eget mauris pharetra et. Nec sagittis aliquam malesuada bibendum arcu vitae elementum curabitur. Phasellus faucibus scelerisque eleifend donec pretium vulputate. Vulputate sapien nec sagittis aliquam. Aliquet lectus proin nibh nisl condimentum id. Quis auctor elit sed vulputate mi sit. Scelerisque eu ultrices vitae auctor eu augue ut lectus arcu. Arcu dui vivamus arcu felis bibendum ut tristique et egestas. Pretium aenean pharetra magna ac placerat. Consectetur purus ut faucibus pulvinar elementum integer enim neque. Vehicula ipsum a arcu cursus vitae congue mauris. Turpis egestas sed tempus urna et. Porttitor lacus luctus accumsan tortor.

Mi sit amet mauris commodo quis imperdiet massa. Nisi porta lorem mollis aliquam. Aenean euismod elementum nisi quis eleifend quam adipiscing. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper. Fames ac turpis egestas integer eget aliquet. Amet nisl suscipit adipiscing bibendum est ultricies. Pellentesque habitant morbi tristique senectus et netus et malesuada. Fusce id velit ut tortor pretium viverra. Blandit massa enim nec dui nunc. Erat nam at lectus urna duis convallis convallis tellus. Faucibus ornare suspendisse sed nisi lacus sed viverra tellus. Orci nulla pellentesque dignissim enim sit amet venenatis urna. Semper feugiat nibh sed pulvinar proin. Vestibulum lectus mauris ultrices eros. Blandit volutpat maecenas volutpat blandit aliquam etiam.

Maecenas sed enim ut sem viverra aliquet eget sit amet. Morbi leo urna molestie at elementum eu facilisis sed. Odio ut enim blandit volutpat maecenas. Amet commodo nulla facilisi nullam vehicula ipsum. Lobortis feugiat vivamus at augue. Amet commodo nulla facilisi nullam vehicula. Felis eget nunc lobortis mattis aliquam. Ante in nibh mauris cursus mattis molestie a. Pulvinar neque laoreet suspendisse interdum consectetur libero. Pretium vulputate sapien nec sagittis aliquam malesuada bibendum. Rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt. Non odio euismod lacinia at. Donec ultrices tincidunt arcu non sodales neque sodales. Dolor sit amet consectetur adipiscing elit duis tristique. Blandit turpis cursus in hac habitasse. Nullam vehicula ipsum a arcu cursus vitae. In metus vulputate eu scelerisque felis imperdiet proin. Placerat duis ultricies lacus sed turpis. Molestie at elementum eu facilisis sed.

Scelerisque viverra mauris in aliquam sem. Sapien pellentesque habitant morbi tristique senectus et netus. Cursus in hac habitasse platea. In dictum non consectetur a erat nam at lectus urna. Mattis molestie a iaculis at erat pellentesque adipiscing commodo elit. Quam adipiscing vitae proin sagittis nisl rhoncus. Augue interdum velit euismod in. Dignissim convallis aenean et tortor. Mattis rhoncus urna neque viverra justo nec ultrices. Auctor eu augue ut lectus. Nisi scelerisque eu ultrices vitae auctor eu. Enim ut sem viverra aliquet. Ut aliquam purus sit amet luctus venenatis lectus magna fringilla. Neque convallis a cras semper auctor. Lectus sit amet est placerat in egestas erat imperdiet sed. Tempus imperdiet nulla malesuada pellentesque elit eget gravida cum sociis. Leo vel fringilla est ullamcorper eget. Nulla aliquet porttitor lacus luctus accumsan tortor.

Montes nascetur ridiculus mus mauris vitae ultricies leo integer malesuada. Vitae auctor eu augue ut lectus arcu bibendum at. Pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper. Mauris augue neque gravida in fermentum. Vulputate odio ut enim blandit volutpat maecenas. Augue ut lectus arcu bibendum at. Pellentesque habitant morbi tristique senectus et netus et malesuada. Nisl nisi scelerisque eu ultrices vitae auctor eu. Blandit libero volutpat sed cras ornare arcu dui. Eu facilisis sed odio morbi. Leo vel orci porta non. Adipiscing commodo elit at imperdiet dui accumsan. Platea dictumst vestibulum rhoncus est pellentesque elit.

Felis imperdiet proin fermentum leo vel orci porta non. Vulputate dignissim suspendisse in est ante in nibh mauris. Bibendum at varius vel pharetra vel turpis nunc eget. Tristique senectus et netus et malesuada fames ac turpis. Enim diam vulputate ut pharetra sit. Sed felis eget velit aliquet sagittis id. Eros donec ac odio tempor orci. Posuere urna nec tincidunt praesent semper feugiat nibh sed pulvinar. In mollis nunc sed id semper risus. Adipiscing elit pellentesque habitant morbi tristique. Sapien faucibus et molestie ac feugiat sed lectus vestibulum mattis.

Diam volutpat commodo sed egestas. Nunc mattis enim ut tellus elementum sagittis vitae et. Sed vulputate odio ut enim blandit volutpat maecenas volutpat. Est lorem ipsum dolor sit. Eu scelerisque felis imperdiet proin. Diam sollicitudin tempor id eu nisl nunc mi ipsum faucibus. Arcu dictum varius duis at consectetur lorem donec massa. Nulla facilisi etiam dignissim diam quis enim lobortis scelerisque. Consectetur adipiscing elit duis tristique sollicitudin nibh sit amet. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien. Consectetur lorem donec massa sapien faucibus et molestie ac. Massa ultricies mi quis hendrerit dolor. Sodales ut eu sem integer vitae justo eget magna. Senectus et netus et malesuada. Laoreet suspendisse interdum consectetur libero id faucibus nisl tincidunt eget. Mi proin sed libero enim sed. Velit dignissim sodales ut eu sem integer vitae justo.

Mauris pellentesque pulvinar pellentesque habitant morbi. Ultrices mi tempus imperdiet nulla malesuada. Ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. Eget felis eget nunc lobortis mattis. Nec ullamcorper sit amet risus nullam eget. Lectus vestibulum mattis ullamcorper velit sed ullamcorper. Laoreet sit amet cursus sit amet dictum sit amet. Est velit egestas dui id ornare arcu odio ut sem. Dapibus ultrices in iaculis nunc sed augue lacus viverra vitae. Pretium viverra suspendisse potenti nullam. Facilisi nullam vehicula ipsum a arcu. Sit amet nisl purus in. Ipsum suspendisse ultrices gravida dictum fusce ut placerat orci nulla. Nunc sed velit dignissim sodales ut eu. Leo integer malesuada nunc vel risus. Sagittis aliquam malesuada bibendum arcu. Risus quis varius quam quisque id diam vel quam elementum. Suscipit adipiscing bibendum est ultricies integer.

Odio ut sem nulla pharetra. Vestibulum lorem sed risus ultricies tristique nulla aliquet enim. Tempor id eu nisl nunc mi ipsum faucibus vitae. Purus non enim praesent elementum facilisis leo vel fringilla est. Sed tempus urna et pharetra pharetra. Lacinia quis vel eros donec ac odio tempor orci. Ac felis donec et odio pellentesque diam volutpat commodo sed. Est ullamcorper eget nulla facilisi etiam dignissim diam. Neque sodales ut etiam sit. Sed viverra tellus in hac. Imperdiet dui accumsan sit amet nulla facilisi morbi tempus. In aliquam sem fringilla ut morbi tincidunt augue interdum velit.

Senectus et netus et malesuada fames ac turpis egestas maecenas. Arcu ac tortor dignissim convallis aenean et. Vitae proin sagittis nisl rhoncus mattis. Auctor urna nunc id cursus. Tincidunt vitae semper quis lectus nulla at volutpat diam ut. Eget velit aliquet sagittis id consectetur purus ut faucibus pulvinar. Maecenas sed enim ut sem viverra aliquet eget sit amet. Iaculis at erat pellentesque adipiscing commodo elit at imperdiet dui. Pellentesque habitant morbi tristique senectus et netus. Feugiat vivamus at augue eget arcu dictum varius duis. Senectus et netus et malesuada fames. Pellentesque pulvinar pellentesque habitant morbi tristique senectus et netus et. Adipiscing at in tellus integer. Nulla pharetra diam sit amet nisl. Condimentum mattis pellentesque id nibh tortor id aliquet lectus proin.

Tellus orci ac auctor augue mauris augue neque. Libero volutpat sed cras ornare arcu dui vivamus. Faucibus vitae aliquet nec ullamcorper sit. Enim lobortis scelerisque fermentum dui faucibus in ornare quam viverra. Purus viverra accumsan in nisl nisi scelerisque eu ultrices vitae. Tortor dignissim convallis aenean et. In hac habitasse platea dictumst vestibulum rhoncus est. Ullamcorper velit sed ullamcorper morbi tincidunt ornare. Pellentesque habitant morbi tristique senectus et netus et malesuada fames. Quisque egestas diam in arcu cursus euismod quis viverra. Ornare arcu odio ut sem nulla pharetra diam sit amet. Accumsan tortor posuere ac ut.

At erat pellentesque adipiscing commodo elit at imperdiet. Vitae congue mauris rhoncus aenean vel elit scelerisque mauris pellentesque. Egestas maecenas pharetra convallis posuere morbi leo urna molestie at. Faucibus et molestie ac feugiat sed lectus vestibulum mattis ullamcorper. Imperdiet dui accumsan sit amet nulla. At urna condimentum mattis pellentesque id. Consequat mauris nunc congue nisi vitae suscipit. Mi in nulla posuere sollicitudin. Vulputate eu scelerisque felis imperdiet. Nibh praesent tristique magna sit amet purus gravida quis blandit. Facilisi nullam vehicula ipsum a arcu cursus vitae congue mauris. Turpis egestas pretium aenean pharetra magna ac placerat. Nulla facilisi cras fermentum odio. Scelerisque fermentum dui faucibus in. Tortor consequat id porta nibh venenatis.

Odio aenean sed adipiscing diam donec adipiscing tristique risus nec. At tellus at urna condimentum mattis pellentesque. Commodo ullamcorper a lacus vestibulum. Urna id volutpat lacus laoreet non curabitur gravida arcu. In aliquam sem fringilla ut. Porta non pulvinar neque laoreet suspendisse. Donec enim diam vulputate ut pharetra sit amet aliquam. Vel fringilla est ullamcorper eget nulla. Parturient montes nascetur ridiculus mus mauris vitae. Neque laoreet suspendisse interdum consectetur libero id faucibus nisl.

Pulvinar elementum integer enim neque volutpat ac tincidunt. Lobortis feugiat vivamus at augue eget arcu dictum. Eget arcu dictum varius duis at consectetur. Nulla porttitor massa id neque aliquam. Mattis vulputate enim nulla aliquet porttitor lacus luctus. Interdum posuere lorem ipsum dolor sit amet. Maecenas ultricies mi eget mauris pharetra et ultrices neque. Aliquet nibh praesent tristique magna sit. Tempus urna et pharetra pharetra massa massa ultricies mi. Arcu dui vivamus arcu felis bibendum ut. Blandit aliquam etiam erat velit scelerisque in dictum non consectetur. Tincidunt id aliquet risus feugiat in ante. Donec massa sapien faucibus et. Dictumst quisque sagittis purus sit. Donec et odio pellentesque diam volutpat commodo. Nullam ac tortor vitae purus faucibus ornare suspendisse. Non arcu risus quis varius. Nec nam aliquam sem et tortor consequat id porta nibh.

Venenatis urna cursus eget nunc scelerisque viverra mauris in aliquam. Rutrum tellus pellentesque eu tincidunt. Ac tortor vitae purus faucibus ornare suspendisse. Blandit aliquam etiam erat velit scelerisque in dictum non consectetur. Sollicitudin ac orci phasellus egestas tellus rutrum. Sit amet luctus venenatis lectus. Felis eget velit aliquet sagittis id consectetur. Nunc scelerisque viverra mauris in. Est placerat in egestas erat imperdiet. Pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum. Amet tellus cras adipiscing enim eu turpis. Nunc mi ipsum faucibus vitae aliquet nec. Nisl nisi scelerisque eu ultrices vitae. Euismod quis viverra nibh cras pulvinar mattis nunc sed blandit. At auctor urna nunc id cursus metus aliquam. At lectus urna duis convallis convallis tellus. Sit amet luctus venenatis lectus magna fringilla urna porttitor. A condimentum vitae sapien pellentesque habitant morbi tristique senectus et. Egestas diam in arcu cursus euismod quis viverra. Nunc vel risus commodo viverra.

Integer feugiat scelerisque varius morbi enim nunc faucibus a pellentesque. Consectetur lorem donec massa sapien faucibus et molestie. Facilisis mauris sit amet massa vitae tortor condimentum lacinia. Vulputate dignissim suspendisse in est ante in nibh mauris. Pulvinar neque laoreet suspendisse interdum. Elit scelerisque mauris pellentesque pulvinar pellentesque habitant. Aliquet nibh praesent tristique magna sit amet purus gravida. Morbi enim nunc faucibus a pellentesque sit amet porttitor eget. In pellentesque massa placerat duis. In hac habitasse platea dictumst quisque sagittis purus sit. Orci sagittis eu volutpat odio facilisis mauris sit. Eget aliquet nibh praesent tristique magna sit.

Nibh mauris cursus mattis molestie a iaculis at erat pellentesque. In ante metus dictum at tempor commodo ullamcorper a. At ultrices mi tempus imperdiet nulla malesuada pellentesque elit. Lectus vestibulum mattis ullamcorper velit sed ullamcorper. Tortor consequat id porta nibh. Tortor dignissim convallis aenean et tortor. At tellus at urna condimentum mattis pellentesque id. Sit amet porttitor eget dolor morbi non arcu risus quis. Quam pellentesque nec nam aliquam sem et tortor consequat. Sed enim ut sem viverra aliquet.

Tempor orci eu lobortis elementum nibh tellus. Placerat duis ultricies lacus sed turpis tincidunt id aliquet. Non diam phasellus vestibulum lorem sed risus ultricies. A arcu cursus vitae congue mauris. Consequat semper viverra nam libero. Lorem ipsum dolor sit amet. Ornare lectus sit amet est placerat in egestas erat imperdiet. Neque volutpat ac tincidunt vitae semper quis lectus. Orci nulla pellentesque dignissim enim sit amet venenatis. Ut diam quam nulla porttitor. Euismod quis viverra nibh cras pulvinar mattis nunc sed. Ac orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt. Donec ultrices tincidunt arcu non sodales neque. Posuere urna nec tincidunt praesent semper feugiat nibh sed pulvinar. Commodo viverra maecenas accumsan lacus vel facilisis volutpat est velit.

Aenean sed adipiscing diam donec. Tristique risus nec feugiat in fermentum posuere. Commodo nulla facilisi nullam vehicula ipsum a arcu cursus vitae. Semper quis lectus nulla at volutpat diam. Aliquet nec ullamcorper sit amet risus. Habitant morbi tristique senectus et netus et malesuada fames. Egestas sed tempus urna et pharetra pharetra massa massa. Eu nisl nunc mi ipsum. Sed blandit libero volutpat sed cras ornare. Mauris ultrices eros in cursus. Ut faucibus pulvinar elementum integer. Scelerisque purus semper eget duis. Commodo odio aenean sed adipiscing diam donec adipiscing tristique. At erat pellentesque adipiscing commodo elit. Fermentum odio eu feugiat pretium nibh ipsum consequat nisl vel. Malesuada proin libero nunc consequat.

Amet est placerat in egestas erat imperdiet. Sit amet tellus cras adipiscing enim eu turpis egestas pretium. Phasellus egestas tellus rutrum tellus pellentesque. Maecenas sed enim ut sem viverra aliquet eget. Odio eu feugiat pretium nibh ipsum consequat nisl vel pretium. Dictum sit amet justo donec enim diam. Tortor posuere ac ut consequat semper viverra nam. Magna ac placerat vestibulum lectus mauris ultrices eros in cursus. Eu augue ut lectus arcu bibendum at. Netus et malesuada fames ac turpis egestas sed. Ut tristique et egestas quis ipsum suspendisse ultrices gravida dictum. Diam phasellus vestibulum lorem sed risus ultricies tristique. Nec dui nunc mattis enim ut.

Amet luctus venenatis lectus magna fringilla. Imperdiet dui accumsan sit amet nulla facilisi. Vestibulum morbi blandit cursus risus at ultrices mi tempus imperdiet. Id venenatis a condimentum vitae sapien. Vitae purus faucibus ornare suspendisse sed nisi. Arcu cursus vitae congue mauris rhoncus. Et sollicitudin ac orci phasellus egestas. Accumsan sit amet nulla facilisi morbi tempus iaculis urna id. Egestas sed sed risus pretium quam vulputate. Dictum varius duis at consectetur lorem donec massa sapien. Convallis a cras semper auctor neque vitae tempus. Dolor sed viverra ipsum nunc aliquet bibendum. Eget duis at tellus at urna condimentum. Facilisi nullam vehicula ipsum a. Diam donec adipiscing tristique risus nec feugiat. Viverra suspendisse potenti nullam ac tortor vitae purus faucibus. Quisque non tellus orci ac auctor augue. Gravida in fermentum et sollicitudin. Luctus venenatis lectus magna fringilla urna porttitor rhoncus dolor. Imperdiet massa tincidunt nunc pulvinar sapien et ligula.

Senectus et netus et malesuada fames ac. Lorem ipsum dolor sit amet consectetur adipiscing elit duis. Sollicitudin ac orci phasellus egestas tellus rutrum tellus pellentesque eu. Vitae elementum curabitur vitae nunc. Amet commodo nulla facilisi nullam vehicula ipsum. Turpis nunc eget lorem dolor sed viverra ipsum. Consectetur adipiscing elit ut aliquam purus. Arcu cursus euismod quis viverra. Ultricies mi quis hendrerit dolor magna eget est. Lectus magna fringilla urna porttitor rhoncus dolor. Auctor augue mauris augue neque gravida in fermentum et sollicitudin. In dictum non consectetur a erat nam. Sed felis eget velit aliquet. Odio ut enim blandit volutpat maecenas volutpat blandit. Aliquet lectus proin nibh nisl condimentum id. Facilisis sed odio morbi quis commodo. Tempus iaculis urna id volutpat lacus laoreet non curabitur gravida.

Blandit libero volutpat sed cras ornare arcu dui vivamus. Sed euismod nisi porta lorem. Aliquam sem et tortor consequat id porta nibh venenatis cras. Ultrices eros in cursus turpis massa. Aliquet porttitor lacus luctus accumsan tortor posuere ac. Neque egestas congue quisque egestas diam. Auctor eu augue ut lectus arcu bibendum at varius vel. Ante metus dictum at tempor commodo ullamcorper a. Velit euismod in pellentesque massa placerat duis ultricies lacus sed. Etiam tempor orci eu lobortis elementum nibh tellus. Pellentesque habitant morbi tristique senectus et netus. Urna porttitor rhoncus dolor purus non enim. Rhoncus dolor purus non enim praesent elementum. Lorem ipsum dolor sit amet consectetur. Est ullamcorper eget nulla facilisi etiam dignissim. Dolor sit amet consectetur adipiscing elit pellentesque habitant morbi. Libero justo laoreet sit amet. Vulputate odio ut enim blandit volutpat maecenas. Faucibus vitae aliquet nec ullamcorper sit amet risus nullam eget. Sagittis orci a scelerisque purus semper eget duis at.

Mauris pharetra et ultrices neque. Placerat vestibulum lectus mauris ultrices eros in cursus turpis. Purus viverra accumsan in nisl nisi scelerisque eu ultrices. Morbi blandit cursus risus at ultrices mi tempus. Aliquet risus feugiat in ante metus dictum at tempor. Amet volutpat consequat mauris nunc congue. Mattis pellentesque id nibh tortor id aliquet lectus proin nibh. Lacus vel facilisis volutpat est velit. Purus non enim praesent elementum facilisis leo vel fringilla. Tellus rutrum tellus pellentesque eu tincidunt. Amet aliquam id diam maecenas ultricies. Eu consequat ac felis donec et odio. Sagittis nisl rhoncus mattis rhoncus. Sit amet cursus sit amet dictum. Amet venenatis urna cursus eget nunc scelerisque. Quisque id diam vel quam elementum pulvinar etiam non. Volutpat ac tincidunt vitae semper quis lectus nulla. Penatibus et magnis dis parturient.

Ut sem viverra aliquet eget sit amet tellus cras. Porta nibh venenatis cras sed felis eget velit aliquet. Amet nisl suscipit adipiscing bibendum. Auctor urna nunc id cursus. Elementum integer enim neque volutpat ac. Lectus sit amet est placerat in egestas. Vitae elementum curabitur vitae nunc sed velit. In fermentum posuere urna nec tincidunt. Eget aliquet nibh praesent tristique magna sit amet purus. Urna id volutpat lacus laoreet non. Augue interdum velit euismod in pellentesque massa placerat. Vulputate dignissim suspendisse in est ante in. Nullam vehicula ipsum a arcu cursus vitae. Suspendisse ultrices gravida dictum fusce. Pellentesque dignissim enim sit amet venenatis urna. Scelerisque purus semper eget duis. Aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices. Mi in nulla posuere sollicitudin aliquam ultrices sagittis orci. Morbi tempus iaculis urna id volutpat lacus laoreet non. Porta non pulvinar neque laoreet suspendisse interdum consectetur libero id.

Metus aliquam eleifend mi in nulla posuere. Pellentesque habitant morbi tristique senectus et netus et. Enim tortor at auctor urna nunc id cursus metus aliquam. Egestas dui id ornare arcu odio ut. Ultrices eros in cursus turpis massa. Congue eu consequat ac felis donec et odio pellentesque. Euismod elementum nisi quis eleifend quam adipiscing vitae proin sagittis. Et ultrices neque ornare aenean euismod elementum. Eu augue ut lectus arcu. Risus nullam eget felis eget nunc lobortis mattis aliquam faucibus.

Donec pretium vulputate sapien nec sagittis aliquam malesuada. Integer quis auctor elit sed vulputate. Id eu nisl nunc mi ipsum faucibus vitae aliquet. Turpis cursus in hac habitasse. Nunc non blandit massa enim nec dui nunc. Id consectetur purus ut faucibus pulvinar elementum integer enim neque. Vitae tempus quam pellentesque nec nam aliquam sem. Penatibus et magnis dis parturient montes. Mattis vulputate enim nulla aliquet porttitor lacus. Adipiscing diam donec adipiscing tristique. Est ante in nibh mauris cursus mattis molestie a. Proin libero nunc consequat interdum varius sit amet. Urna id volutpat lacus laoreet non curabitur gravida arcu ac. Nunc sed id semper risus. Quam viverra orci sagittis eu volutpat. Integer enim neque volutpat ac tincidunt.

Erat nam at lectus urna duis convallis convallis tellus id. Nunc sed augue lacus viverra vitae congue eu consequat. Volutpat diam ut venenatis tellus in metus. Maecenas volutpat blandit aliquam etiam erat. Egestas quis ipsum suspendisse ultrices. Est ullamcorper eget nulla facilisi etiam. Vitae aliquet nec ullamcorper sit amet risus nullam eget. Varius morbi enim nunc faucibus a pellentesque sit amet porttitor. Tristique magna sit amet purus gravida quis. Sit amet luctus venenatis lectus magna fringilla. Posuere urna nec tincidunt praesent semper feugiat nibh. Amet purus gravida quis blandit turpis cursus in hac habitasse. Arcu bibendum at varius vel. Turpis in eu mi bibendum neque egestas congue quisque. Arcu non sodales neque sodales ut etiam. Dui vivamus arcu felis bibendum.

Pretium viverra suspendisse potenti nullam ac tortor vitae purus faucibus. Nunc sed id semper risus. Sed ullamcorper morbi tincidunt ornare. Egestas egestas fringilla phasellus faucibus scelerisque eleifend. Aliquam id diam maecenas ultricies mi. Tincidunt tortor aliquam nulla facilisi cras fermentum. Blandit cursus risus at ultrices. Dignissim convallis aenean et tortor at risus viverra adipiscing at. Adipiscing tristique risus nec feugiat in fermentum posuere. Quam pellentesque nec nam aliquam. Ut tristique et egestas quis ipsum. Ac felis donec et odio pellentesque diam. Tempor id eu nisl nunc mi ipsum faucibus vitae.

Quam quisque id diam vel quam elementum pulvinar etiam. Venenatis a condimentum vitae sapien pellentesque habitant morbi tristique. Arcu bibendum at varius vel pharetra vel turpis nunc. Vel turpis nunc eget lorem. Risus ultricies tristique nulla aliquet enim tortor. Nam at lectus urna duis convallis convallis tellus id interdum. Erat nam at lectus urna duis convallis convallis. Imperdiet proin fermentum leo vel orci porta. Est velit egestas dui id ornare arcu odio ut sem. Mi proin sed libero enim sed faucibus turpis in eu. Pulvinar pellentesque habitant morbi tristique senectus et netus et. Bibendum neque egestas congue quisque egestas diam in arcu cursus. Porta lorem mollis aliquam ut porttitor leo a diam. Cras fermentum odio eu feugiat. Aliquam malesuada bibendum arcu vitae. Turpis in eu mi bibendum neque egestas congue quisque egestas.

Ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget gravida. Gravida neque convallis a cras. Turpis egestas integer eget aliquet nibh praesent tristique magna. Donec ac odio tempor orci dapibus ultrices in. Ipsum dolor sit amet consectetur adipiscing elit pellentesque. Mauris cursus mattis molestie a iaculis at erat pellentesque. Elit at imperdiet dui accumsan. Massa vitae tortor condimentum lacinia quis vel eros. Diam vulputate ut pharetra sit amet aliquam. Dolor purus non enim praesent elementum facilisis leo. Tellus cras adipiscing enim eu turpis egestas pretium aenean pharetra. Luctus accumsan tortor posuere ac ut consequat semper viverra. Etiam dignissim diam quis enim lobortis. Fusce ut placerat orci nulla pellentesque dignissim enim. In eu mi bibendum neque. Fermentum dui faucibus in ornare. Ultrices neque ornare aenean euismod elementum nisi quis eleifend.

Lobortis feugiat vivamus at augue eget arcu dictum varius. Tempus iaculis urna id volutpat lacus. Eu volutpat odio facilisis mauris sit amet massa. Mattis molestie a iaculis at. Aenean pharetra magna ac placerat vestibulum lectus mauris. Quisque id diam vel quam elementum pulvinar etiam non. Ut diam quam nulla porttitor massa id. Pharetra magna ac placerat vestibulum. Maecenas volutpat blandit aliquam etiam erat velit scelerisque in dictum. Cursus euismod quis viverra nibh cras pulvinar mattis nunc. Ac ut consequat semper viverra. Enim eu turpis egestas pretium aenean pharetra magna.

Morbi non arcu risus quis varius quam quisque id. Sodales neque sodales ut etiam sit amet nisl. Malesuada pellentesque elit eget gravida cum sociis natoque penatibus et. Fringilla phasellus faucibus scelerisque eleifend donec pretium. At lectus urna duis convallis convallis tellus id interdum velit. Amet consectetur adipiscing elit ut aliquam purus sit amet. At erat pellentesque adipiscing commodo elit at. Porta non pulvinar neque laoreet suspendisse interdum consectetur libero id. Pellentesque diam volutpat commodo sed egestas egestas fringilla. Eget aliquet nibh praesent tristique magna sit amet purus gravida. Lorem mollis aliquam ut porttitor leo. Massa id neque aliquam vestibulum morbi blandit. Amet mattis vulputate enim nulla aliquet porttitor lacus luctus. A pellentesque sit amet porttitor eget dolor morbi. Vulputate enim nulla aliquet porttitor lacus. Accumsan sit amet nulla facilisi morbi tempus.

Suscipit tellus mauris a diam maecenas sed. Nulla facilisi cras fermentum odio eu feugiat pretium nibh. Lectus sit amet est placerat in egestas erat imperdiet. Integer malesuada nunc vel risus commodo viverra maecenas accumsan. In iaculis nunc sed augue lacus. Sit amet est placerat in egestas erat imperdiet. Vulputate mi sit amet mauris. Nullam eget felis eget nunc lobortis mattis aliquam. Nulla facilisi cras fermentum odio eu feugiat pretium nibh. Feugiat nisl pretium fusce id velit.

Venenatis tellus in metus vulputate. Leo vel fringilla est ullamcorper eget nulla facilisi etiam. Varius morbi enim nunc faucibus a. Sed velit dignissim sodales ut eu sem integer. A iaculis at erat pellentesque adipiscing commodo elit at imperdiet. At auctor urna nunc id. Quam viverra orci sagittis eu volutpat. Proin fermentum leo vel orci porta non. Nulla porttitor massa id neque aliquam. Justo eget magna fermentum iaculis eu non. Vestibulum rhoncus est pellentesque elit ullamcorper dignissim. Diam phasellus vestibulum lorem sed risus ultricies tristique.

Scelerisque purus semper eget duis at tellus at urna condimentum. Ut aliquam purus sit amet luctus venenatis. Tincidunt nunc pulvinar sapien et. Ultrices vitae auctor eu augue ut lectus arcu bibendum at. Ac orci phasellus egestas tellus rutrum. Volutpat est velit egestas dui. Elit sed vulputate mi sit amet mauris commodo quis imperdiet. Nibh mauris cursus mattis molestie a. Lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant. Elementum integer enim neque volutpat ac tincidunt. Condimentum lacinia quis vel eros donec ac odio tempor. Sit amet nisl suscipit adipiscing bibendum. Enim neque volutpat ac tincidunt. A scelerisque purus semper eget duis. Placerat orci nulla pellentesque dignissim. Duis ut diam quam nulla porttitor massa id. Pretium quam vulputate dignissim suspendisse in est ante. Nam at lectus urna duis convallis. Neque sodales ut etiam sit amet nisl purus. Turpis egestas maecenas pharetra convallis posuere.

Ultrices gravida dictum fusce ut placerat orci nulla pellentesque. Est ultricies integer quis auctor elit sed vulputate mi. Enim facilisis gravida neque convallis a cras. Cras ornare arcu dui vivamus arcu felis. Pharetra diam sit amet nisl suscipit adipiscing bibendum. Eget duis at tellus at urna. In hac habitasse platea dictumst. Massa ultricies mi quis hendrerit dolor. Faucibus in ornare quam viverra orci sagittis. Vel quam elementum pulvinar etiam non. Diam sit amet nisl suscipit adipiscing bibendum est ultricies. Nec feugiat nisl pretium fusce. Proin sagittis nisl rhoncus mattis rhoncus urna neque viverra. Ac turpis egestas integer eget aliquet nibh praesent. Consectetur adipiscing elit pellentesque habitant. Nunc non blandit massa enim nec dui nunc mattis. Quis blandit turpis cursus in hac habitasse. Pellentesque massa placerat duis ultricies lacus sed. Id cursus metus aliquam eleifend mi in. Quam pellentesque nec nam aliquam sem et tortor consequat.

Porta nibh venenatis cras sed felis eget. Orci nulla pellentesque dignissim enim. Malesuada pellentesque elit eget gravida cum sociis natoque penatibus. Velit ut tortor pretium viverra suspendisse potenti nullam ac. Vulputate mi sit amet mauris commodo quis imperdiet massa. At imperdiet dui accumsan sit amet nulla. Consectetur adipiscing elit pellentesque habitant morbi tristique senectus. Iaculis eu non diam phasellus. Velit sed ullamcorper morbi tincidunt ornare massa eget egestas purus. Gravida dictum fusce ut placerat orci nulla pellentesque dignissim enim. Tellus id interdum velit laoreet id donec ultrices. Scelerisque felis imperdiet proin fermentum.

Tincidunt eget nullam non nisi est sit amet. Etiam sit amet nisl purus. Euismod in pellentesque massa placerat. Est ultricies integer quis auctor elit sed vulputate mi. Etiam non quam lacus suspendisse faucibus interdum posuere. Nunc pulvinar sapien et ligula ullamcorper malesuada proin libero nunc. Pellentesque habitant morbi tristique senectus et netus et malesuada. Integer quis auctor elit sed. At augue eget arcu dictum. At risus viverra adipiscing at in tellus integer feugiat scelerisque. Eget est lorem ipsum dolor sit amet consectetur adipiscing. Cursus sit amet dictum sit amet justo.

Quis ipsum suspendisse ultrices gravida dictum fusce ut placerat orci. Sed turpis tincidunt id aliquet risus feugiat in ante. Porttitor eget dolor morbi non arcu risus quis varius. Nibh sit amet commodo nulla facilisi nullam. Tincidunt id aliquet risus feugiat in ante metus dictum. Vitae congue eu consequat ac felis. Velit sed ullamcorper morbi tincidunt ornare massa eget egestas purus. Ullamcorper a lacus vestibulum sed arcu non odio euismod. Cras tincidunt lobortis feugiat vivamus at augue eget arcu dictum. Risus viverra adipiscing at in tellus integer feugiat scelerisque varius. Nunc congue nisi vitae suscipit tellus mauris a. Euismod nisi porta lorem mollis aliquam ut porttitor leo. Nunc eget lorem dolor sed viverra ipsum.

Vestibulum morbi blandit cursus risus at ultrices mi. Sit amet mauris commodo quis imperdiet massa tincidunt. Sed odio morbi quis commodo odio aenean sed. Quis blandit turpis cursus in hac habitasse platea. In tellus integer feugiat scelerisque. Blandit cursus risus at ultrices mi tempus imperdiet nulla. Malesuada proin libero nunc consequat interdum varius sit amet mattis. Nisl nunc mi ipsum faucibus vitae. Montes nascetur ridiculus mus mauris. Risus ultricies tristique nulla aliquet enim tortor. Ut consequat semper viverra nam libero justo.

Arcu non sodales neque sodales ut etiam. Id diam maecenas ultricies mi eget mauris pharetra. Ut aliquam purus sit amet luctus venenatis lectus magna. Diam sit amet nisl suscipit adipiscing. Blandit cursus risus at ultrices mi tempus imperdiet. Eu sem integer vitae justo eget magna fermentum. Diam maecenas sed enim ut. Ut tristique et egestas quis ipsum suspendisse. Magna ac placerat vestibulum lectus mauris. Nulla aliquet enim tortor at auctor. Congue mauris rhoncus aenean vel. Porttitor eget dolor morbi non arcu risus quis varius quam. Egestas dui id ornare arcu odio ut sem. Curabitur gravida arcu ac tortor dignissim. Nunc eget lorem dolor sed. Et netus et malesuada fames ac turpis. Risus commodo viverra maecenas accumsan lacus vel facilisis volutpat est. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Mollis aliquam ut porttitor leo a diam sollicitudin.

Vitae congue mauris rhoncus aenean vel elit scelerisque mauris pellentesque. Bibendum at varius vel pharetra vel turpis. Turpis cursus in hac habitasse. Vel fringilla est ullamcorper eget nulla facilisi etiam dignissim diam. Aliquet eget sit amet tellus cras adipiscing enim eu turpis. Eget velit aliquet sagittis id consectetur. Bibendum est ultricies integer quis auctor elit sed vulputate mi. Eros donec ac odio tempor orci dapibus. Amet volutpat consequat mauris nunc congue nisi vitae suscipit. Sit amet nulla facilisi morbi tempus iaculis urna. Neque aliquam vestibulum morbi blandit cursus risus at. Cursus risus at ultrices mi tempus imperdiet nulla malesuada. Nisl pretium fusce id velit ut tortor pretium viverra. Pellentesque pulvinar pellentesque habitant morbi tristique senectus et netus et. Id volutpat lacus laoreet non. Sagittis eu volutpat odio facilisis mauris sit amet massa. Aliquam ultrices sagittis orci a scelerisque purus semper eget. Bibendum neque egestas congue quisque egestas diam in arcu. A scelerisque purus semper eget duis at tellus at. Nunc pulvinar sapien et ligula ullamcorper.

Est ullamcorper eget nulla facilisi etiam. Ut pharetra sit amet aliquam id diam maecenas ultricies mi. Euismod in pellentesque massa placerat duis ultricies lacus sed. Enim diam vulputate ut pharetra sit. Aenean pharetra magna ac placerat vestibulum lectus. Ac orci phasellus egestas tellus rutrum tellus. Amet purus gravida quis blandit turpis cursus in hac habitasse. Fringilla urna porttitor rhoncus dolor purus non enim praesent elementum. In fermentum et sollicitudin ac orci phasellus egestas. Orci a scelerisque purus semper eget duis at tellus. Aliquet nibh praesent tristique magna sit. Varius sit amet mattis vulputate enim nulla. Nullam vehicula ipsum a arcu. Tellus in hac habitasse platea dictumst vestibulum rhoncus. In nulla posuere sollicitudin aliquam ultrices. Augue ut lectus arcu bibendum at.

Quam viverra orci sagittis eu volutpat odio facilisis mauris. Blandit turpis cursus in hac habitasse platea dictumst quisque sagittis. Metus dictum at tempor commodo ullamcorper. Tincidunt tortor aliquam nulla facilisi cras fermentum odio eu feugiat. Sed pulvinar proin gravida hendrerit lectus a. Aenean euismod elementum nisi quis eleifend quam adipiscing vitae. Nisl nisi scelerisque eu ultrices vitae auctor eu augue. Lorem ipsum dolor sit amet consectetur. Integer feugiat scelerisque varius morbi enim nunc faucibus. Id semper risus in hendrerit gravida rutrum quisque. Turpis nunc eget lorem dolor sed viverra ipsum nunc.

Neque convallis a cras semper auctor. Mi sit amet mauris commodo quis imperdiet. Velit aliquet sagittis id consectetur. Malesuada nunc vel risus commodo. Aenean et tortor at risus viverra. Vestibulum lorem sed risus ultricies tristique. Consectetur adipiscing elit ut aliquam purus sit amet luctus. Egestas quis ipsum suspendisse ultrices gravida dictum fusce ut. Elementum integer enim neque volutpat ac tincidunt vitae semper quis. Id interdum velit laoreet id. Ornare arcu dui vivamus arcu. Luctus venenatis lectus magna fringilla urna porttitor rhoncus. Integer vitae justo eget magna fermentum iaculis. Molestie nunc non blandit massa enim nec dui nunc. Viverra aliquet eget sit amet tellus cras adipiscing enim eu. Sed libero enim sed faucibus turpis in eu. Commodo viverra maecenas accumsan lacus. Duis tristique sollicitudin nibh sit amet commodo. Et tortor consequat id porta nibh venenatis.

Neque convallis a cras semper auctor. Mi sit amet mauris commodo quis imperdiet. Velit aliquet sagittis id consectetur. Malesuada nunc vel risus commodo. Aenean et tortor at risus viverra. Vestibulum lorem sed risus ultricies tristique. Consectetur adipiscing elit ut aliquam purus sit amet luctus. Egestas quis ipsum suspendisse ultrices gravida dictum fusce ut. Elementum integer enim neque volutpat ac tincidunt vitae semper quis. Id interdum velit laoreet id. Ornare arcu dui vivamus arcu. Luctus venenatis lectus magna fringilla urna porttitor rhoncus. Integer vitae justo eget magna fermentum iaculis. Molestie nunc non blandit massa enim nec dui nunc. Viverra aliquet eget sit amet tellus cras adipiscing enim eu. Sed libero enim sed faucibus turpis in eu. Commodo viverra maecenas accumsan lacus. Duis tristique sollicitudin nibh sit amet commodo. Et tortor consequat id porta nibh venenatis.

`;
	import { onMount, tick } from "svelte";
	import { get } from "svelte/store";

	import { browser } from "$app/env";
	import { page } from "$app/stores";

	import { captureEndpoint } from "$urls/restEndpoints";
	import { responsiveMode } from "$store/responsive";
	import { projectName } from "$lib/constants/frontend/projectName";
	import { isUserAuthenticated, userToken } from "$store/users";
	import { snakeCaseToTitleCase } from "$lib/functions/snakeCaseToTitleCase";
	import anime from "animejs";

	$: episode_number = parseInt($page.params.number);
	$: anime_name = snakeCaseToTitleCase($page.params.anime_name);

	let player: HTMLVmPlayerElement;
	let showPlayer = false;
	let captionEnabled = true;

	onMount(async () => {
		const { defineCustomElements } = await import("@vime/core");
		defineCustomElements();
		showPlayer = true;
	});

	// PLayer hooks
	$: {
		if (player) {
			const localStorageVideoVolume =
				parseInt(browser && localStorage.getItem("vimejs-volume")) || 100;
			player.volume = localStorageVideoVolume;
		}
	}

	const onVolumeChange = async () => {
		if (browser) {
			localStorage.setItem("vimejs-volume", JSON.stringify(~~player?.volume));

			if ($isUserAuthenticated) {
				try {
					fetch(captureEndpoint, {
						method: "PATCH",
						headers: {
							Accept: "application/json",
							"Content-Type": "application/json",
							Authorization: `Bearer ${get(userToken).access}`
						},
						body: JSON.stringify({
							video_volume: ~~player?.volume
						})
					});
				} catch {
					console.error(`POST to ${captureEndpoint} Failed`);
				}
			}
		}
	};

	const handleKeydown = async (event: KeyboardEvent) => {
		/*
			Maps Keys to vimejs control

				* Space | K 	= 	Play / Pause
				* M 			= 	Mute / Unmute
				* C				= 	Captions
				* ArrowRight 	= 	Seek Forward 5 sec
				* ArrowLeft 	= 	Seek Backward 5 sec
				* F				= 	Enter / Exit FullScreen
		
		*/

		switch (event?.key?.toLowerCase()) {
			case " ":
			case "k": {
				player?.paused ? player?.play() : player?.pause();
				break;
			}
			case "m": {
				player?.muted ? player?.removeAttribute("muted") : player?.setAttribute("muted", "");
				break;
			}
			case "c": {
				switch (captionEnabled) {
					case true: {
						await player?.setTextTrackVisibility(false);
						captionEnabled = false;
						break;
					}
					case false: {
						await player?.setTextTrackVisibility(true);
						captionEnabled = true;
						break;
					}
				}
				break;
			}
			case "arrowright": {
				player.currentTime += 5;
				break;
			}
			case "arrowleft": {
				player.currentTime -= 5;
				break;
			}
			case "f": {
				player?.isFullscreenActive ? player?.exitFullscreen() : player?.enterFullscreen();
				break;
			}
		}
	};

	let showMore = false;
	let chevronOne: HTMLElement;
	let chevronTwo: HTMLElement;

	let textContentParagraph: HTMLParagraphElement;
	let textContentParagraphHeight = 0;

	$: {
		let height = textContentParagraph?.clientHeight;
		if (height > textContentParagraphHeight) {
			textContentParagraphHeight = height;
		}
	}

	$: switch (showMore) {
		case true:
			if (browser && chevronOne && chevronTwo && textContentParagraph) {
				anime({
					targets: [chevronOne],
					rotate: [0, 180],
					easing: "easeOutSine",
					duration: 500
				});

				anime({
					targets: [chevronTwo],
					rotate: [0, -180],
					easing: "easeOutSine",
					duration: 500
				});

				anime({
					targets: [textContentParagraph],
					height: ~~textContentParagraphHeight,
					duration: 500,
					easing: "linear"
				});
			}
			break;
		case false:
			if (browser && chevronOne && chevronTwo && textContentParagraph) {
				anime({
					targets: [chevronOne, chevronTwo],
					rotate: [180, 0],
					easing: "easeOutSine",
					duration: 500
				});

				anime({
					targets: [chevronTwo],
					rotate: [-180, 0],
					easing: "easeOutSine",
					duration: 500
				});

				anime({
					targets: [textContentParagraph],
					height: 100,
					duration: 500,
					easing: "linear"
				});
			}
	}
</script>

<svelte:window on:keydown={handleKeydown} />

<svelte:head>
	<title>{anime_name} | Episode : {episode_number} | {projectName}</title>
</svelte:head>

<div class="container pt-5">
	{#if showPlayer}
		<vm-player autoplay bind:this={player} on:vmVolumeChange={onVolumeChange}>
			<vm-video poster="https://media.vimejs.com/poster.png" cross-origin>
				<source data-src="https://media.vimejs.com/720p.mp4" type="video/mp4" />
				<track default kind="subtitles" src="/media/subs/en.vtt" srclang="en" label="English" />
			</vm-video>
			<vm-default-ui />
		</vm-player>
	{:else}
		<section class="hero is-large">
			<div class="hero-body">
				<div class="has-text-centered">
					<button class="button is-ghost is-loading is-size-2" />
				</div>
			</div>
		</section>
	{/if}
</div>
<div class="container pt-5">
	<!-- Main container -->
	<nav class="level is-mobile">
		<!-- Left side -->
		<div
			class="level-left {$responsiveMode === 'mobile'
				? 'is-size-6'
				: 'is-size-4'} {$responsiveMode === 'mobile' ? 'pl-4' : ''}"
		>
			<div class="level-item">
				<a
					href="/anime/{$page.params.anime_name}/episode/{episode_number - 1}"
					sveltekit:prefetch
					sveltekit:noscroll
				>
					<ion-icon name="arrow-back-outline" class="has-text-white" />
				</a>
			</div>
		</div>

		<!-- Middle side -->
		<div class="level-item">
			<p class="has-text-white {$responsiveMode === 'mobile' ? 'is-size-6' : 'is-size-4'}">
				Anime Name : {anime_name} | Episode :
				{episode_number}
			</p>
		</div>

		<!-- Right side -->
		<div
			class="level-right {$responsiveMode === 'mobile'
				? 'is-size-6'
				: 'is-size-4'} {$responsiveMode === 'mobile' ? 'pr-4' : ''}"
		>
			<p class="level-item">
				<a
					href="/anime/{$page.params.anime_name}/episode/{episode_number + 1}"
					sveltekit:prefetch
					sveltekit:noscroll
				>
					<ion-icon name="arrow-forward-outline" class="has-text-white" />
				</a>
			</p>
		</div>
	</nav>
</div>
<div class="container">
	<div
		class="column is-flex {$responsiveMode === 'desktop' ||
		$responsiveMode === 'widescreen' ||
		$responsiveMode === 'fullhd'
			? ''
			: 'is-align-self-center'}"
	>
		<div class="content has-text-white">
			<h1 class="has-text-white">Synopsis :</h1>
			<p bind:this={textContentParagraph} class="is-clipped has-text-justified">
				{textContent}
			</p>
			<!-- Main container -->
			<nav class="level is-mobile">
				<!-- Middle side -->
				<div class="level-item">
					<div
						class="has-text-white is-clickable"
						on:click={() => {
							showMore = !showMore;
						}}
					>
						<ion-icon bind:this={chevronOne} name="chevron-down-outline" />
						<span class="pb-5 {$responsiveMode === 'mobile' ? 'is-size-5' : 'is-size-4'}">
							Show More
						</span>
						<ion-icon bind:this={chevronTwo} name="chevron-down-outline" />
					</div>
				</div>
			</nav>
		</div>
	</div>
</div>
