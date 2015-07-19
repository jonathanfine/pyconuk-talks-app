TEMPLATE = '''\
<html>
<head>
  <link rel='stylesheet' href='talks.css'>
  <script src='./local/jquery-1.11.3.js' type='text/javascript'></script>
  <script src='./talks.js' type='text/javascript'></script>
  <script src="./local/jquery-ui-1.11.4/jquery-ui.js"></script>
</head>
<body>

<h2>PyCon 2015 Talks</h2>

<div class='controls'>
<p class='by-score'>
Score:
<span class='by-score-all'>All</span>
<span class='by-score-0'>0</span>
<span class='by-score-1'>1</span>
<span class='by-score-2'>2</span>
<span class='by-score-3'>3</span>
</p>

<p class='by-category'>
Category:
<span class='by-category-all'>All</span>
<span class='by-category-1'>One</span>
<span class='by-category-2'>Two</span>
<span class='by-category-3'>Three</span>
</p>
</div>

<div id='talks'>
{talks}
</div>

</body>
</html>
'''


talk = '''\
<div id='talk-{number}' class='talk score-{score}'>
<h3>
<span class='star-0'>0</span>
<span class='star-1'>1</span>
<span class='star-2'>2</span>
<span class='star-3'>3</span>
Title etc for talk {number}.
</h3>
</div>
<div>
<p>Abstract for talk {number}.</p>
</div>
'''.format


if __name__ == '__main__':

    talks = '\n'.join(talk(score=0, number=i) for i in range(1, 11))
    html = TEMPLATE.format(talks=talks)

    with open('talks.html', 'w') as f:
        f.write(html)
