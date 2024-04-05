import obsws_python as obs

cl = obs.ReqClient(host='localhost', port=4455, password='g1UjucGuxLbACh2H', timeout=3)

scene = cl.send("GetSceneItemList", data="Scene", raw=True)
print(scene)
#scene = scene["scenes"][1]["sceneName"]
#cl.create_scene_item(scene, "browserSource")
