<template>
  <nav class='navbar navbar-expand-lg navbar-dark container bg-dark navigation col-12'>
    <a class='navbar-brand' style='color: #34afb0' href='#broken'>meet codejam</a>
    <button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarsExample09' aria-controls='navbarsExample09'
      aria-expanded='false' aria-label='Toggle navigation'>
      <span class='navbar-toggler-icon'></span>
    </button>

    <div class='collapse navbar-collapse' id='navbarsExample09'>
      <ul class='navbar-nav mr-auto'>
        <li class='nav-item'>
          <a class='nav-link' href='#broken'>leaderboard</a>
        </li>
          <li class='nav-item'>
            <a class='nav-link' href='#broken'>problems</a>
          </li>
          <li class='nav-item'>
            <a class='nav-link' href='#broken'>team</a>
          </li>
      </ul>
      <ul class='navbar-nav ml-auto'>
        <li class='nav-item'>
          <!-- {% if session['user_id'] %} -->
          <a class='nav-link' href='#broken'>sign out</a>
          <!-- {% else %}
          <a class='nav-link' href='#broken'>sign in</a>
          {%endif%} -->
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style lang="scss" scoped>
.navbar {
  margin-bottom: 60px;
}
</style>
