%global username dci-labs

Name:           dci-labs-ssh-pubkeys
Version:        0.1
Release:        1%{?dist}

Summary:        DCI Labs members public SSH keys
License:        ASL2.0
URL:            https://github.com/dci-labs/ssh-pubkeys

BuildArch:      noarch

Requires(pre):  shadow-utils
Requires:       sudo

%description
This package contains the SSH public keys of the DCI Labs team members

%prep

%build

%install
install -d  %{buildroot}/%{_sysconfdir}/sudoers.d
install -d -m 700 %{buildroot}/home/%{username}/.ssh
cat > %{buildroot}/home/%{username}/.ssh/authorized_keys <<EOF
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC3twoI7N5bprilj5zmU2SVdOv79n9sHHKt9aZrRKBwc6mg62w+4gW54E36vHgxkJmkL3MTOQzxzEj2NxUgJ9qWKkicjV5/2wuyc/aSQIni6F+zAyIsyenfweiIMbd0qR+Cv5JpKIDjW/7EviaC3qBnGi4V9kMMhdaQLKbpVQQkfoAbjoH5ndnXUaG00+w0vErAGxJJqcwZIzhIfTfwfBcvhMCaMMd/zohOeQzZnMy/je26c6WN56mc31xb/uXWnjzy5vAjk+cxvlv/KpM1UtwyB8DLXdk/uOkL1q9vHAeRt4ClQfAuTeyFTccDB4GBiNFzxv11+nOAQQWIjhA5HXTjhH8yU8B2mdIeLSnVKfHlOka44zcsa0/B1n9fjmNOyRHVPX+Ks8pAGgNLy++m5kGNr2FtORZtOfFIseNWok4LaNBP3WRnW2n3uQa0EalHmRjJ1datW3Fu6Sv1N5keqZW5fXfgdrypgdqoMudLmqsXW7DsI/nqE/e1Mud8WI53HwIuSHpBD7KLP70m0R8PjWw+dkn5cffZVYwPOI1f0Q3Jkbz5x3Rmq9Pug/ncwU8mZu9hCxgn8ZlZ7rv6HmrWm+msmB6LvPsUJMmnFypwDHXYtMDPGNiQE10Ek9EsIoHP/41ppD73oFpDbxF6Tg8Q0YYMCtmAwyw1dgcud7N3Gq4bNw== jgallego@redhat.com
EOF

cat > %{buildroot}/%{_sysconfdir}/sudoers.d/%{username} <<EOF
%{username} ALL=(ALL) NOPASSWD:ALL
EOF

%files
%attr(0440, root, root) %{_sysconfdir}/sudoers.d/%{username}
%attr(0700, %{username}, %{username}) /home/%{username}/.ssh
%attr(0600, %{username}, %{username}) /home/%{username}/.ssh/authorized_keys

%pre
getent group %{username} >/dev/null || groupadd -r %{username}
getent passwd %{username} >/dev/null || \
    useradd -r -g %{username} -d /home/%{username} -s /bin/bash \
    -c "The DCI Labs user" -m %{username}
exit 0

%changelog
* Wed Jul 07 2021 Jorge A Gallegos <jgallego@redhat.com> - 0.1-1
- Initial implementation

