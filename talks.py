TEMPLATE = '''\
<html>
<head>
  <link rel='stylesheet' href='talks.css'>
  <script src='./local/jquery-1.11.3.js' type='text/javascript'></script>
  <script src='./talks.js' type='text/javascript'></script>
</head>
<body>

<p>Hello</p>

{talks}

</body>
</html>
'''


talk = '''\
<div class='talk score-{score}'>
<span class='star-0'>0</span>
<span class='star-1'>1</span>
<span class='star-2'>2</span>
<span class='star-3'>3</span>
</div>
'''.format


if __name__ == '__main__':

    talks = '\n'.join(talk(score=i) for i in range(4))
    html = TEMPLATE.format(talks=talks)

    with open('talks.html', 'w') as f:
        f.write(html)
