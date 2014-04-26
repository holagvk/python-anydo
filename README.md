python-anydo
============

Unofficial python bindings for Any.Do, an attractive todo list organizer.

[![Build Status](https://travis-ci.org/gvkalra/python-anydo.png?branch=master)](https://travis-ci.org/gvkalra/python-anydo)
[![Coverage Status](https://coveralls.io/repos/gvkalra/python-anydo/badge.png?branch=master)](https://coveralls.io/r/gvkalra/python-anydo?branch=master)

The bindings cooperate with the official applications available viz:

[![Google Play](http://www.any.do/images/download-badges/40px/googleplay.png)](https://play.google.com/store/apps/details?id=com.anydo)
[![App Store](http://www.any.do/images/download-badges/40px/appstore.png)](https://itunes.apple.com/us/app/any.do/id497328576?ls=1&mt=8)
[![Chrome Web Store](http://www.any.do/images/download-badges/40px/chromewebstore.png)](https://chrome.google.com/webstore/detail/anydo/kdadialhpiikehpdeejjeiikopddkjem)

Usage Guide
-----------------
Authenticate to Any.Do and create AnyDoAPI object
```python
from anydo.api import AnyDoAPI
api = AnyDoAPI(username='username@example.org', password='password')
```

**Get User Information**
```python
api.get_user_info()
```

**Get All Tasks (including Notes)**
```python
api.get_all_tasks()
```

**Get Task/Note by ID**
```python
api.get_task_by_id()
```

**Delete Task/Note by ID**
```python
api.delete_task_by_id()
```

**Get All Categories**
```python
api.get_all_categories()
```

**Delete Category by ID**
```python
api.delete_category_by_id()
```

**Create new category**
```python
api.create_new_category()
```

**Create new task**
```python
api.create_new_task()
```

Developing python-anydo
--------------------------------------------
You should add bin/runtest.sh as pre-commit git-hook.
It will help you in verifying your changes locally.
```bash
$ git clone https://github.com/gvkalra/python-anydo.git
$ cd python-anydo
$ cp bin/runtest.sh .git/hooks/pre-commit
```

License
-----------------
```text
The MIT License (MIT)

Copyright (c) 2014 Gaurav Kalra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

Authors
-----------------
- Gaurav Kalra (<gvkalra@gmail.com>)
- Kouhei Maeda (<mkouhei@gmail.com>)
