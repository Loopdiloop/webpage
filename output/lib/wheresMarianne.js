/* start module: wheresMarianne */
$pyjs['loaded_modules']['wheresMarianne'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['wheresMarianne']['__was_initialized__']) return $pyjs['loaded_modules']['wheresMarianne'];
	var $m = $pyjs['loaded_modules']['wheresMarianne'];
	$m['__repr__'] = function() { return '<module: wheresMarianne>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'wheresMarianne';
	$m['__name__'] = __mod_name__;


	$m['pyjs'] = $p['___import___']('pyjs', null);
	$m['Scraping'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'wheresMarianne';
		$method = $pyjs__bind_method2('__init__', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('scrape', function(N) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				N = arguments[1];
			}
			var timestamp,tree,tweets,page;
			page = $m['requests']['get']('https://twitter.com/MarianneKontor');
			tree = $m['html']['fromstring']($p['getattr'](page, 'content'));
			tweets = tree['xpath']('//p[@class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]/text()');
			timestamp = tree['xpath']('//span[@class="_timestamp js-short-timestamp js-relative-timestamp"]/text()');
			return $p['tuple']([tweets['__getitem__'](N), timestamp['__getitem__'](N)]);
		}
	, 1, [null,null,['self'],['N']]);
		$cls_definition['scrape'] = $method;
		var $bases = new Array(pyjslib['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('Scraping', $p['tuple']($bases), $data);
	})();
	$p['printFunc']([$m['Functions']()['scrape']()], 1);
	return this;
}; /* end wheresMarianne */


/* end module: wheresMarianne */


/*
PYJS_DEPS: ['pyjs']
*/
