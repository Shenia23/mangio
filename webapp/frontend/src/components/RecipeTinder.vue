<template>
  
</template>

<script>
import Tinder from "vue-tinder";

export default {
  name: "App",
  components: { Tinder },
  data: () => ({
    
  }),
 
  methods: {
    mock(count = 5, append = true) {
      const list = [];
      for (let i = 0; i < count; i++) {
        list.push({ id: this.sources[this.offset] });
        this.offset++;
      }
      if (append) {
        this.queue = this.queue.concat(list);
      } else {
        this.queue.unshift(...list);
      }
    },
    onSubmit({ item }) {
      if (this.queue.length < 3) {
        this.mock();
      }
      this.history.push(item);
    },
    async decide(choice) {
      if (choice === "rewind") {
        if (this.history.length) {
          this.$refs.tinder.rewind([this.history.pop()]);
        }
      } else if (choice === "help") {
        window.open("https://shanlh.github.io/vue-tinder");
      } else {
        this.$refs.tinder.decide(choice);
      }
    },
  },
};
</script>

<style>
html,
body {
  height: 100%;
}

body {
  margin: 0;
  background-color: #20262e;
  overflow: hidden;
}

.nope-pointer,
.like-pointer {
  position: absolute;
  z-index: 1;
  top: 20px;
  width: 64px;
  height: 64px;
}

.nope-pointer {
  right: 10px;
}

.like-pointer {
  left: 10px;
}

.super-pointer {
  position: absolute;
  z-index: 1;
  bottom: 80px;
  left: 0;
  right: 0;
  margin: auto;
  width: 112px;
  height: 78px;
}

.rewind-pointer {
  position: absolute;
  z-index: 1;
  top: 20px;
  right: 10px;
  width: 112px;
  height: 78px;
}

.pic {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
}

.btns img {
  margin-right: 12px;
  box-shadow: 0 4px 9px rgba(0, 0, 0, 0.15);
  border-radius: 50%;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.btns img:nth-child(2n + 1) {
  width: 53px;
}

.btns img:nth-child(2n) {
  width: 65px;
}

.btns img:nth-last-child(1) {
  margin-right: 0;
}
.vue-tinder {
  position: absolute;
  z-index: 1;
  left: 0;
  right: 0;
  top: 23px;
  bottom: 46px;
  margin: auto;
  min-width: 300px;
  max-width: 355px;
}
</style>