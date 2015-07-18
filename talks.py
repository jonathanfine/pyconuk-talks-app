TEMPLATE = '''\
<html>
<head>
  <link rel='stylesheet' href='talks.css'>
  <script src='./local/jquery-1.11.3.js' type='text/javascript'></script>
  <script src='./talks.js' type='text/javascript'></script>
</head>
<body>

<h2>PyCon 2015 Talks</h2>

{talks}

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
'''.format


if __name__ == '__main__':

    talks = '\n'.join(talk(score=0, number=i) for i in range(1, 11))
    html = TEMPLATE.format(talks=talks)

    with open('talks.html', 'w') as f:
        f.write(html)
