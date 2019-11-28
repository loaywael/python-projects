import json


class CacheIt:

    def __init__(self, req_func):
        self.func = req_func
        self.func.__name__ = req_func.__name__
        self.name = None
        self.cache = None
        self.temp = {}

    def open_cache(self, op=None, mode="r", **buffer):

        print("Opening file: cache.json")

        self.cache = open("cache.json", mode, encoding="utf-8")
        print("Cache is open with mode: ({})".format(mode))

        if op:

            if op == "read":
                cachedData = self.read_cache(buffer["name"])
                self.cache.close()
                return cachedData

            elif op == "update":
                self.update_cache(buffer["resp"])

            elif op == "append":
                self.append_cache(buffer["name"], buffer["resp"])

            elif op == "clean":
                with open("cache.json", "w"):
                    pass

            else:
                print("operation not found, try again:")
                print("choose operation from:\n{}".format("=" * 50))
                print("{'read', 'update', 'append', 'clean', 'content'}")
                exit  # terminates the program used for testing
        self.cache.close()

    def check_cache(self):

        try:
            with open("cache.json", "r"):
                print("Cache file was found and open in read mode")
                return "found"

        except IOError as e:
            print("{} >> file not found!".format(e))
            with open("cache.json", "w"):
                print("Created the cache file: cache.json")
                return None

    def check_empty_cache(self):
        with open("cache.json", "r") as ch:
            ch.seek(0)
            first_chr = ch.read(100)
            if not first_chr:
                print("Cache file is empty.")
                return False
            else:
                return True

    def read_cache(self, name):

        self.temp = {}
        self.name = name
        self.temp = json.load(self.cache)  # load cache memory
        print("Loaded the cache successfully!")
        print("searching in cache memory..")
        if self.name not in self.temp:  # check name in cache
            print("The movie was not found in cache memory!")
            return None

        else:
            print("The movie was found in cache memory.")
            cachedData = self.temp[self.name]  # return response data
            return cachedData

    def search_cache(self, target):

        if target not in self.temp[self.name]:
            print("Target ({}) wasn't found!".format(target))
            return None

        else:
            print("Extracting Data..")
            respData = self.temp[self.name][target]["data"]
            return respData

    def update_cache(self, buffer):
        # when name is found but need to update it's content
        newResp = {self.func.__name__: buffer}
        self.temp[self.name].update(newResp)
        print("Successfully updated cache for ({}): {}".format(self.name, self.temp[self.name].keys()))
        json.dump(self.temp, fp=self.cache, indent=4, ensure_ascii=False)

    def append_cache(self, name, buffer):
        # when name not found it add it with new data
        self.name = name
        newResp = {self.func.__name__: buffer}
        self.temp[self.name] = newResp  # add request response to cache memory
        print("Adding content to the cache file..")
        json.dump(self.temp, fp=self.cache, indent=4, ensure_ascii=False)
        print("Appended ({}) to the cache file!".format(self.name))
        self.temp = {}

    def __call__(self, *args, **kwargs):

        name = args[0].upper()
        cachedData = content = respData = newResp = None
        sortTitle = self.func.__name__
        fileState = self.check_cache()
        content = self.check_empty_cache()

        if fileState == "found" and content:  # file found and not empty
            cachedData = self.open_cache(op="read", name=name)  # read from cache update buffer

        if not cachedData:  # if name not in cache data=None
            print("Requesting new Response from the web..")
            newResp = self.func(*args, **kwargs)  # request new response
            self.open_cache(mode="w", op="append", name=name, resp=newResp)  # add new response to cache
            respData = newResp["data"]  # extract data and end event
            return respData  # end event

        else:  # if name in cache >> load buffer with response saved in cache
            respData = self.search_cache(sortTitle)  # extract data from response
            if not respData:  # if data not matching request target
                newResp = self.func(*args, **kwargs)  # request new response
                self.open_cache(op="update", mode="w", resp=newResp)  # update (append to) existing name response
                # extract data from new updated response and end event
                respData = newResp["data"]
                return respData  # end event
            # Executed when the target matches the response in cache
            return respData  # end event