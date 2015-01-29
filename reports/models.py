from django.db import models


report_choices = ((u'\u0631\u0634\u0648\u0629', u'\u0631\u0634\u0648\u0629'),  # bribe
                  (u'\u062a\u0632\u0648\u064a\u0631', u'\u062a\u0632\u0648\u064a\u0631'),  # fraud
                  (u'\u0645\u062d\u0633\u0648\u0628\u064a\u0629', u'\u0645\u062d\u0633\u0648\u0628\u064a\u0629'),  # favor
                  (u'\u0625\u062e\u0644\u0627\u0644 \u0628\u0627\u0644\u0648\u0627\u062c\u0628 \u0627\u0644\u0645\u0647\u0646\u064a', u'\u0625\u062e\u0644\u0627\u0644 \u0628\u0627\u0644\u0648\u0627\u062c\u0628 \u0627\u0644\u0645\u0647\u0646\u064a'),  # breach
                  (u'\u0625\u062e\u062a\u0644\u0627\u0633', u'\u0625\u062e\u062a\u0644\u0627\u0633'),  # embez
                  (u'\u062a\u062c\u0627\u0648\u0632\u0627\u062a \u0622\u062e\u0631\u0649', u'\u062a\u062c\u0627\u0648\u0632\u0627\u062a \u0622\u062e\u0631\u0649'))  # other

report_status = (
                (u'\u0641\u064a \u0625\u0646\u062a\u0638\u0627\u0631 \u0627\u0644\u0645\u0648\u0627\u0641\u0642\u0629', u'\u0641\u064a \u0625\u0646\u062a\u0638\u0627\u0631 \u0627\u0644\u0645\u0648\u0627\u0641\u0642\u0629'),  # pending
                (u'\u062a\u0645\u062a \u0627\u0644\u0645\u0648\u0627\u0641\u0642\u0629', u'\u062a\u0645\u062a \u0627\u0644\u0645\u0648\u0627\u0641\u0642\u0629'),  # approved
                (u'\u0642\u064a\u062f \u0627\u0644\u062a\u062a\u0628\u0639', u'\u0642\u064a\u062f \u0627\u0644\u062a\u062a\u0628\u0639'),  # in progress
                (u'\u062d\u0644\u062a', u'\u062d\u0644\u062a'),)  # solved

gov_choices = (
    ('Ariana', 'Ariana'),
    ('Beja', 'Beja'),
    ('Ben Arous', 'Ben Arous'),
    ('Bizerte', 'Bizerte'),
    ('Gabes', 'Gabes'),
    ('Gafsa', 'Gafsa'),
    ('Jendouba', 'Jendouba'),
    ('Kairouan', 'Kairouan'),
    ('Kasserine', 'Kasserine'),
    ('Kebili', 'Kebili'),
    ('Kef', 'Kef'),
    ('Mahdia', 'Mahdia'),
    ('Manouba', 'Manouba'),
    ('Medenine', 'Medenine'),
    ('Monastir', 'Monastir'),
    ('Nabeul', 'Nabeul'),
    ('Sfax', 'Sfax'),
    ('Sidi Bouzid', 'Sidi Bouzid'),
    ('Siliana', 'Siliana'),
    ('Sousse', 'Sousse'),
    ('Tataouine', 'Tataouine'),
    ('Tozeur', 'Tozeur'),
    ('Tunis', 'Tunis'),
    ('Zaghouan', 'Zaghouan'),
)


class Report(models.Model):
    title = models.CharField(u'\u0627\u0644\u0639\u0646\u0648\u0627\u0646', max_length=128)
    full_name = models.CharField(u'\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628', max_length=128)
    cin = models.CharField(u'\u0631\u0642\u0645 \u0628 \u062a \u0648', max_length=8)
    job = models.CharField(u'\u0627\u0644\u0645\u0647\u0646\u0629', max_length=128)
    type = models.CharField(u'\u0646\u0648\u0639 \u0627\u0644\u0628\u0644\u0627\u063a', choices=report_choices, max_length=128)
    tel = models.IntegerField(u'\u0631\u0642\u0645 \u0627\u0644\u0647\u0627\u062a\u0641')
    description = models.TextField(u'\u062a\u0641\u0627\u0635\u064a\u0644', blank=True)
    votes = models.IntegerField(default=0, null=True)
    justify = models.FileField(u'\u0623\u062f\u0644\u0629', upload_to='media/justify/', blank=True)
    status = models.CharField(choices=report_status, max_length=128, default=u'pending_approval\u0641\u064a \u0625\u0646\u062a\u0638\u0627\u0631 \u0627\u0644\u0645\u0648\u0627\u0641\u0642\u0629', blank=True)
    gouvernorat = models.CharField(u'\u0627\u0644\u0648\u0644\u0627\u064a\u0629', max_length=128, choices=gov_choices, default='pending_approval')

    def __unicode__(self):
            return self.title


class Advice(models.Model):
    type = models.CharField(max_length=129, choices=report_choices)
    content = models.TextField(blank=True)

    def __unicode__(self):
        return self.type