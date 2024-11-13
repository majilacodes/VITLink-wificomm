self.addEventListener('push', function(event) {
    const data = event.data.json();
    const title = data.title || 'Notification';
    const options = {
        body: data.body,
        icon: 'icon.png', // Path to an icon image
        badge: 'badge.png' // Path to a badge image
    };
    event.waitUntil(
        self.registration.showNotification(title, options)
    );
});
