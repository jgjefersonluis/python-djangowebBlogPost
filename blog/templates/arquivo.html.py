{% for post in posts %}

	<h2> {{ post.title }} </h2>
		<p>{{ post.time }}</p>
		<p>{{ post.body }}</p>
		
{% endfor %}